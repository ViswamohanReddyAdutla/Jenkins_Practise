*** Settings ***


*** Variables ***

${Name}    My Name
${Loc}    India

*** Test Cases ***

PrintNameandLocation
    [Documentation]   Priniting both Name and Location from the variables Section
    log    ${Name}
    log    ${Loc}
