*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Surf To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  testaaja
    Set Password  testaaja123
    Set Password Confirmation  testaaja123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testaaja123
    Set Password Confirmation  testaaja123
    Submit Credentials
    Register Should Fail With Message  Username too short, must be at least 3 letters

Register With Valid Username And Invalid Password
    Set Username  tester
    Set Password  testaaja
    Set Password Confirmation  testaaja
    Submit Credentials
    Register Should Fail With Message  Password must consist of letters a-z and at least one number 0-9

Register With Nonmatching Password And Password Confirmation
    Set Username  tester
    Set Password  testaaja123
    Set Password Confirmation  testaaja1
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match
    

*** Keywords ***
Register Should Succeed
    Register Succeeded Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}    

Surf To Register Page
    Go To Register Page
    Register Page Should Be Open