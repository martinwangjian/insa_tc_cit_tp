# Session 0
How to authenticate with AWS SSO to AWS Console?

## Change password

1. You should have received an email with title `Invitation to join AWS Single Sign-On` from `no-reply@login.awsapps.com` Click on `Accept invitation`
![](img/sso_invitation.png)

1. __Set new password__
![](img/sso_set_password.png)

1. __Sign in__ with your new password
![](img/sso_sign_in.png)

## Set up MFA
1. Select __Authenticator app__
![](img/sso_mfa_1.png)

1. Install a Multi-factor authentication (MFA) application on you smartphone, For example, `Google Authenticator` 

1. __Show QR code__, scan with your authenticator app and enter 6 digit __Authenticator code__ then __Assgign MFA__
![](img/sso_mfa_2.png)
![](img/sso_mfa_3.png)

1. __Sign in__ with your User portal URL (`https://xxx.awsapps.com/start`) with your password and MFA
![](img/sso_sign_in.png)

## Use AWS Console

1. Select `account<your group ID>`
![](img/sso_account_1.png)

1. You are now using AS Console of your account, select `Ireland` as region
![](img/sso_account_2.png)

1. Select `English(US)` as language of AWS Console
![](img/sso_account_3.png)