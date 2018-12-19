""" It's possible to add all users in your organization to a group.
This is a feature which you can find in the Admin console group management.
When adding all users it creates a single member with type="CUSTOMER" in the group.

This script will brute force through the memberships to tell you which groups
    have all users as a member.

If you have a large number of groups or memberships then you may need to 
    make changes to stay within your quota.

Running this script will output 1 row for each group to stdout.
Each row contains 3 values separated by commas.
{group email},{has all users 'Yes' or 'No'}

Please follow the steps in the Readme file to complete the authorization 
    requirements needed to run this script.
"""

from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete and regenerate the file token.json.
SCOPES = 'https://www.googleapis.com/auth/admin.directory.group.readonly'

def main():
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('admin', 'directory_v1', http=creds.authorize(Http()))

    # Call the Admin SDK groups.list API to get all groups and paginate
    #   through the results.
    nextPageToken = None
    while True:
        results = service.groups().list(customer='my_customer',
                                        maxResults=200,
                                        pageToken=nextPageToken).execute()
        groups = results.get('groups', [])

        for group in groups:
            has_all_users = membership_has_all_users(service, group)
            print(u'{0},{1}'.format(group['email'], 'Yes' if has_all_users else 'No'))

        nextPageToken = results.get('nextPageToken')
        if nextPageToken is None: 
            # We've reached the last page and there are no more groups
            break

def membership_has_all_users(service, group):
    # Call the AdminSDK members.list API to get all members and paginate
    #   through the results.
    # Returns True once it finds type="CUSTOMER" else False
    nextPageToken = None
    while True:
        results = service.members().list(groupKey=group['id'],
                                        maxResults=200,
                                        pageToken=nextPageToken).execute()
        members = results.get('members', [])
        for member in members:
            if member['type'] == 'CUSTOMER':
                return True

        nextPageToken = results.get('nextPageToken')
        if nextPageToken is None: 
            # We've reached the last page and there are no more memberships
            break

    return False

if __name__ == '__main__':
    main()
