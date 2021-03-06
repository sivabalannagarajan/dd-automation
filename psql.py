from datadog import initialize, api
import json

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key,support_mail, access_key, secret_key, slack_channels, customer_email_id, postgresql_connections, postgresql_locks, alerts_list):

    options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
    }
    initialize(**options)
    options = dict(notify_no_data=False, no_data_timeframe=0)
    options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
    tags = 'datadog'

    if "psql" in alerts_list:
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:postgresql.connections{*} by {host,name,region} >" + str(postgresql_connections),
                       name="["+str(customer_name)+"]" + " - " + "PSQL connection is high",
                       message="Team,PSQL connection is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:postgresql.connections{*} by {host,name,region} >" + str(postgresql_connections),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "PSQL connection is high",
                       message="Team,PSQL connection is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),
#locks
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:postgresql.locks{*} by {host,name,region} >" + str(postgresql_locks),
                       name="["+str(customer_name)+"]" + " - " + "PSQL lock found",
                       message="Team,PSQL lock found. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:postgresql.locks{*} by {host,name,region} >" + str(postgresql_locks),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "PSQL lock found",
                       message="Team,PSQL lock found. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),
            return True