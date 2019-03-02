# AdminSDK, List All Groups In Customer

This script uses the AdminSDK to list all groups in your customer.

## Prerequisites

Clone this repository.

```
mkdir all-groups-in-customer
cd all-groups-in-customer
git clone https://github.com/jmathai-google/all-groups-in-customer.git ./
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
some-group@yourdomain.com
some-other-group@yourdomain.com
mygroup1@yourdomain.com
mygroup2@yourdomain.com
....
mygroup1000@yourdomain.com

# If you'd like to count the total number of groups you can run the following command.
python run.py | wc -l
      18
```

You may want to call `python run.py > all-groups-in-customer.csv` to import it into a spreadsheet.
