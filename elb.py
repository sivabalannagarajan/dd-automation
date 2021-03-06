from datadog import initialize, api
import json

def get_all_input_fields_and_add_to_data_dog(customer_name, api_key, app_key,support_mail, access_key, secret_key, slack_channels, customer_email_id,
                                             elb_httpcode_backend_4xx, elb_httpcode_backend_5xx, alerts_list):

    options = {
            'api_key': str(api_key),
            'app_key': str(app_key)
    }
    initialize(**options)
    options = dict(notify_no_data=False, no_data_timeframe=0)
    options2 = dict(notify_no_data=False, no_data_timeframe=0, renotify_interval=10)
    tags = 'datadog'

    #ELB - Unhealthy Host
    try:
        if "elb" in alerts_list:
            print json.dumps(api.Monitor.create(type="metric alert",
                   query="min(last_5m):avg:aws.elb.un_healthy_host_count{*} by {hostname,region} > 0",
                   name="["+str(customer_name)+"]" + " - " + "Unhealthy insatnce found on this ELB",
                   message="Team,Unhealthy insatnce found on this ELB. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                   tags=tags,
                   options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:aws.elb.un_healthy_host_count{*} by {hostname,region} > 0",
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "Unhealthy insatnce found on this ELB",
                       message="Team,Unhealthy insatnce found on this ELB. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),
# #ELB - 4xx Count
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:aws.elb.httpcode_backend_4xx{*} by {hostname,region} >"+str(elb_httpcode_backend_4xx),
                       name="["+str(customer_name)+"]" + " - " + "ELB 4XX count is high",
                       message="Team,ELB 4XX count is high on this ELB. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:aws.elb.httpcode_backend_4xx{*} by {hostname,region} > 20",
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "ELB 4XX count is high",
                       message="Team,ELB 4XX count is high on this ELB. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),
# #ELB - 5xx Count
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:aws.elb.httpcode_backend_5xx{*} by {hostname,region} >"+str(elb_httpcode_backend_5xx),
                       name="["+str(customer_name)+"]" + " - " + "ELB 5XX count is high",
                       message="Team,ELB 5XX count is high on this ELB. Please take a look into this." + " @"+"cloudops@minjar.com " + str(slack_channels) + " @"+str(customer_email_id) ,
                       tags=tags,
                       options=options2)),
            print json.dumps(api.Monitor.create(type="metric alert",
                       query="min(last_5m):avg:aws.elb.httpcode_backend_5xx{*} by {hostname,region} > 20",
                       name="[Ticket]" + " - " + "["+str(customer_name)+"]" + " - " + "ELB 5XX count is high",
                       message="Team,ELB 5XX count is high on this ELB. Please take a look into this. @"+str(support_mail),
                       tags=tags,
                       options=options)),
        return True
    except Exception as e:
        print e
        return False