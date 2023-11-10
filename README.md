# 42_logtime_counter_PERSO
An application to calculate the logtime of month

# Tutorial 
## Introduction 
Using the [42 API tool](https://api.intra.42.fr/apidoc), we are going to to make some GET request with [curl](https://curl.se/) and receive a JSON data.

## Get credentials
To use 42 API we need to create an application then use our **u-id** and **s-id**.
[Here is the getting started documentation](https://api.intra.42.fr/apidoc/guides/getting_started). 

1) Connect to your 42 profile then go the API settings page [here](https://profile.intra.42.fr/oauth/applications/new).
2) Create your new application `Register a new app`.
3) Now you have UID and a secret ID

### Get access token
Now that you have your UID and secret ID we can try curl command to get the access token.</br>
```BASH
curl -X POST --data "grant_type=client_credentials&client_id=MY_AWESOME_UID&client_secret=MY_AWESOME_SECRET" https://api.intra.42.fr/oauth/token
```
You have to chang `MY_AWESOME_UID` by your **UID** and `MY_AWESOME_SECRET` by your **secret ID**.

And voila you got your **access_token** !

### Get token info
Your first request can be asking more info about your access_token.

```BASH
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" https://api.intra.42.fr/oauth/token/info
```
You have to change `YOUR_ACCESS_TOKEN` by your **access_token**. </br>
You have the expire time of your token in seconds.

## Get locations stats info
You can ask for the locations and logtime info of a chosen user with his login. [Here is the user location data](https://api.intra.42.fr/apidoc/2.0/users/locations_stats.html)

```BASH
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" "https://api.intra.42.fr/v2/users/atchougo/locations_stats"
```
You can add `begin_at` and `end_at` params to specify data. </br>
```BASH
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" "https://api.intra.42.fr/v2/users/atchougo/locations_stats?begin_at=2023-11-01&end_at=2023-11-30"
```
You have to change `YOUR_ACCESS_TOKEN` by your access_token. </br>
