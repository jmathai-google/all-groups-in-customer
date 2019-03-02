""" The groups.list API returns a paginated result which makes it possible
    to list all the groups in a customer.

    If you have a large number of groups then you may need to 
    make changes to stay within your quota.

    Running this script will output 1 row for each group to stdout.

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
            print(u'{0}'.format(group['email']))

        nextPageToken = results.get('nextPageToken')
        if nextPageToken is None: 
            # We've reached the last page and there are no more groups
            break

if __name__ == '__main__':
    main()
