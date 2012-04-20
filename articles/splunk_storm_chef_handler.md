### Overview

Using my [Chef Exception & Reporting Handler for Splunk Storm](https://github.com/ampledata/chef_handler/tree/feature/COOK-1208_splunkstorm_handler)
you can easily search for and report on your chef-client runs.


### Steps

1. Create a [Splunk Storm](https://www.splunkstorm.com) account.
2. Retrieve your Splunk Storm [REST API Credentials](http://docs.splunk.com/Documentation/Storm/Beta/User/UseStormsRESTAPI).
3. Download the [chef_handler](https://github.com/ampledata/chef_handler/tree/feature/COOK-1208_splunkstorm_handler) Cookbook.
4. Add the **chef_handler** Cookbook to your Run List.
5. Given you've retrieved your Access Token as **ACCESS_TOKEN** and Project ID
as **PROJECT_ID**, add a chef_handler Resource to one of your Recipes:

        :::ruby
        chef_handler 'SplunkStorm::SplunkStormHandler' do
          action :enable
          source File.join(node['chef_handler']['handler_path'], 'splunkstorm.rb')
          arguments ['ACCESS_TOKEN', 'PROJECT_ID']
        end

### Usage
#### Search

A search for * should result in events like these:

![chef-client report in Splunk Storm](http://dl.dropbox.com/u/4036736/Screenshots/h2hc.png)

#### Report

The following dashboard shows the **Average chef-client Elapsed Time by Host**:

![Average chef-client Elapsed Time by Host](http://dl.dropbox.com/u/4036736/Screenshots/qx9j.png)

Here's the assocaited search:

    * | spath path=elapsed_time output=elapsed_time | timechart span="15m" avg(elapsed_time) by host
