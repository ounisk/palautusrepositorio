*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    #Input New Command  # ei tätä tähän enää
    Input Credentials  tester  tester12345  
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input Credentials  testaaja  123tester
    Output Should Contain  User with username testaaja already exists


Register With Too Short Username And Valid Password
    Input Credentials  te  123tester
    Output Should Contain  Username too short, must be at least 3 letters


Register With Enough Long But Invald Username And Valid Password
    Input Credentials  12345  123tester
    Output Should Contain  Username must consist of letters a-z


Register With Valid Username And Too Short Password
    Input Credentials  tester  1r
    Output Should Contain  Password too short, must be at least 8 characters


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  tester  salasana
    Output Should Contain  Password must consist of letters a-z and at least one number 0-9


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  testaaja  testaaja2
    
    