*** Settings ***
Library     SeleniumLibrary




*** Keywords ***
Poprawne Logowanie
    open browser    https://pl.wikipedia.org    chrome
    wait until element is visible   pt-login  3   Jest blad
    click element   pt-login
    ${my_value}     get text        wpName1
    should be empty  ${my_value}
    input text      wpName1     RobotTests
    ${my_value}  get text  //*[@id="wpPassword1"]
    input password    //*[@id="wpPassword1"]  RobotFramework
    checkbox should not be selected     wpRemember
    select checkbox     wpRemember
    click button        wpLoginAttempt
    #capture page screenshot   screen.png
    sleep           3
    close browser




*** Variables ***

${error_message}  Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.



*** Test Cases ***
Nieudane logowanie
    open browser    https://pl.wikipedia.org    chrome
    wait until element is visible   pt-login  3   Jest blad
    click element   pt-login
    ${my_value}     get text        wpName1
    should be empty  ${my_value}
    input text      wpName1     RobotTests
    ${my_value}  get text  //*[@id="wpPassword1"]
    input password    //*[@id="wpPassword1"]  123123
    checkbox should not be selected     wpRemember
    select checkbox     wpRemember
    click button        wpLoginAttempt
    wait until element is visible   //*[@id="userloginForm"]/form/div[1]
    ${my_error_message}    get text  //*[@id="userloginForm"]/form/div[1]
    log to console      ${my_error_message}
    log  ${my_error_message}
    should be equal as strings  ${my_error_message}  ${error_message}
    capture page screenshot   screen.png
    sleep           3
    close browser


