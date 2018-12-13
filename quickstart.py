from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/admin.directory.group.readonly'

def main():
    """Shows basic usage of the Admin SDK Directory API.
    Prints the emails and names of the first 10 users in the domain.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('admin', 'directory_v1', http=creds.authorize(Http()))

    # Call the Admin SDK Directory API
    print('Listing all groups with all users as member')
    nextPageToken = None
    while True:
        results = service.groups().list(customer='my_customer',
                                        maxResults=200,
                                        pageToken=nextPageToken).execute()
        groups = results.get('groups', [])

        if not groups:
            print('No groups in the domain.')
        else:
            for group in groups:
                #print(u'{0} ({1})'.format(group['id'],
                #    group['email']))
                has_all_users = membership_has_all_users(service, group)
                print(u'{0},{1}'.format(group['email'], 'Yes' if has_all_users else 'No'))

        nextPageToken = results.get('nextPageToken')
        if nextPageToken is None: 
            #print(u'No more groups')
            break
        break

def membership_has_all_users(service, group):
    #print(u'Listing all members of {0}'.format(group['email']))
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
            #print(u'No more members')
            break

    return False

if __name__ == '__main__':
    main()
