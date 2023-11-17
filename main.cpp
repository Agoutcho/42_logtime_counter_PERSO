#include <iostream>
#include <chrono>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace date;

int main() {
   // Step 1: Get the access token
   CURL* curl = curl_easy_init();
   if(curl) {
       curl_easy_setopt(curl, CURLOPT_URL, "https://api.intra.42.fr/oauth/token");
       curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "grant_type=client_credentials&client_id=MY_AWESOME_UID&client_secret=MY_AWESOME_SECRET");
       // ... continue setting options ...
       CURLcode res = curl_easy_perform(curl);
       // ... check for errors and handle response ...
   }
   curl_easy_cleanup(curl);

   // Step 2: Make the API request
   // ... similar to Step 1, but with different options ...

   // Step 3: Parse the JSON response
   json j = json::parse(response); // replace 'response' with the actual response string

   // Step 4: Calculate the total hours
   std::chrono::hours totalHours(0);
   for(auto& [date, hours] : j.items()) {
       // Parse the hours string into a duration
       std::chrono::hours hoursDuration = std::chrono::duration_cast<std::chrono::hours>(parse_hh_mm_ss(hours));
       totalHours += hoursDuration;
   }

   // Step 5: Print the result
   std::cout << "Total hours spent in the month: " << totalHours.count() << std::endl;

   return 0;
}

