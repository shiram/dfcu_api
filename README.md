# DFCU_API
Authenticate the user with the system and obtain the auth_token
Request
Method
URL            
POST
api/accounts/loans/



Type
Params
Values
HEAD
POST
Auth token
Account number


string
string



Auth Token
 An Authentication token  must be sent with all client requests. The token helps the server to validate and authorize the request source.

Account Number
 An account  must be sent with all client requests. This is the account number which is validated and whose loans are sent in response.


Response
Status
Response
200
{
   "response": {
       "customer_id": "C003",
       "customer_name": "James Blunt",
       "customer_account": "5000145080",
       "customer_loans": [
           {
               "loan_id": "L000005",
               "disbursement_date": "2023-02-16T12:24:54Z",
               "outstanding_amount": 500000
           }
       ]
   }
}



auth_key (string) - all further API calls must have this key in header
401
{"error":"Invalid Auth Token."}
500
{"error":"Something went wrong. Please try again later."}

