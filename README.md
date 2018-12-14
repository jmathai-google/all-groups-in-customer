# AdminSDK, List Groups With All Users In Customer

This script uses the AdminSDK to list all groups which contain "all users in my organization". View the [support article](https://support.google.com/a/answer/6191469?hl=en&visit_id=636804153881207464-2829703435&rd=1) to learn more about this feature.

## Prerequisites

Clone this repository.

```
mkdir groups-with-all-users-in-customer
cd groups-with-all-users-in-customer
git clone https://github.com/jmathai-google/groups-with-all-users-in-customer.git ./
```

You'll need python 2.7 installed to run this script. It's recommended that you run this command inside of a `virtualenv`.

```
pip install -r requirements.txt
```

## Set up authentication and authorization

Follow [these steps](https://developers.google.com/admin-sdk/directory/v1/quickstart/python) to set up authentication and authorization. This script will require you to log in with a user who has the admin role to read all groups in your customer.

## Run the script

Here is a sample output of running the script.

The first time you run this script it will open your browser and ask you to sign in. Make sure you sign in with an account that has admin privileges to read all groups in your customer. Once you sign in and grant your script access you can close your browser and return to your terminal. This stores a file named `token.json` and you will not need to authenticate again as long as that file is in your directory.

```
python run.py
some-group@yourdomain.com,Yes
some-other-group@yourdomain.com,No
mygroup1@yourdomain.com,No
mygroup2@yourdomain.com,No
....
mygroup1000@yourdomain.com,Yes
```

Every row with the second column as `Yes` contains all users in your organization as a member.

You may want to call `python run.py > groups-with-all-users.csv` to import it into a spreadsheet.
