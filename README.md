# Simple Flask server to execute python scripts.

## [POST] - /api/run

### Request json:

-   script : python script
-   argv : arguments

### Response json:

-   res : console output of the script
-   error : error message in case of error
