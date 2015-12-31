from datadog import initialize, api
import json

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key,support_mail, access_key, secret_key, slack_channels, customer_email_id, connections, alerts_list):

    options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
    }
    initialize(**options)
    options = dict(notify_no_data=False, no_data_timeframe=0)
    options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
    tags = 'datadog'

    if "activemq" in alerts_list:
            api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:nginx.net.connections{*} by {host,name,region} >" + str(connections),
                       name="["+str(customer_name)+"]" + " - " + "JVM Thread count is high",
                       message="Team,JVM Thread count is high. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2),
            api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:nginx.net.connections{*} by {host,name,region} >" + str(connections),
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "JVM Thread count is high",
                       message="Team,JVM Thread count is high. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options),
            api.Monitor.create(type="metric alert",
                       query="min(last_30m):avg:nginx.net.connections{*} by {host,name,region} >" + str(connections),
                       name="[Escalation-TL]" + " - " + "["+str(customer_name)+"]" + " - " + "JVM Thread count is high",
                       message="Team,JVM Thread count is high. Please take a look into this. @cloudops-business@minjar.com ",
                       tags=tags,
                       options=options),
            api.Monitor.create(type="metric alert",
                       query="min(last_1h):avg:nginx.net.connections{*} by {host,name,region} >" + str(connections),
                       name="[Escalation]" + " - " + "["+str(customer_name)+"]" + " - " + "JVM Thread count is high",
                       message="Team,JVM Thread count is high. Please take a look into this. @cloudops-business@minjar.com ",
                       tags=tags,
                       options=options),
            return True