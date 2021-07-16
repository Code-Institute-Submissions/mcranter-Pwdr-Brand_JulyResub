## Testing
### Manual Testing.
### Functionality

1. Search function: Home Page
    - Tested search fuctionality by submitting an empty search in order to verify that an error message appeared.
    - Result: An error message appeared, displaying the text: 'Error! You didn't enter any search criteria!'
    ![](media/test-search-none.png)


    - Tested search functionality for accuracy by submitting legitimate search for various whole terms ('berry', 'workout' etc.) with all  inputs valid.

    - Result: All expected search items were returned.
    ![](media/test-terms.png)


    - Tested search functionality by submitting searches for shortened terms of three and two letters (such as 'ber''wor','ba') to see if all relevent items were returned.
    - Result: All expected search items were returned. 
    ![](media/test-search-small.png)


2. Login Page:
    - Tested login functionality by submitting incorrect login details in order to verify that an error message appeared.
    - Result: Error message appeared displaying the text: 'The username and/or password you specified are not correct.'
    ![](media/login-username.png)

3. Register Page
    - Tested registration functionality by attempting to log in using an existing username in order to verify an error message appeared.
    - Result: The registration page refreshed and displayed an error saying 'A user with that username already exists.'
    ![](media/test-reg-name.png)
   
    - Tested registraion functionality by attempting to log in using an existing email address in order to verify an error message appeared.
    - Result: The registration page refreshed and displayed an error saying 'A user is already registered with this e-mail address.'
    ![](media/test-reg-email.png)

    - Tested registration functionality by attempting to register a username using fewer than 4 letters in order to verify that an error message appeared.
    - Result: Error message is diplayed, reading 'Please lengthen this text to 4 characters or more (you are currently using 3')
    ![](media/test-signup3.png)


4. Product Page:
    - Attempt to add a number of products exceeding 99.
    - Attempt to click on a sum of zero products.

5. Checkout Page:
    - Attempt to enter an email address without an @ symbol to trigger an error.
    - Attempt to include text in the phone numbers field to trigger an error.
    - Enter invalid credit card number - this will trigger an error.