# Canvas API for score submission

For TAs easily submit scores to Canvas

## Procedures
- get your access token

1. Go to canvas, click left side bannar and go to your account setting. 
![get_token_0][GetToken0]

2. In integration part, click "New Access Token" to add a new token. Type a label for it, and set a expiration date. **Be careful: it is not recommended to set token a long time. You may increase the token leaking danger**. The best way is, when you need one, you generate one for single day only.
![get_token_1][GetToken1]

3. Copy the token, you will need it for the API calls. **Caution: do not share it to anyone or spread it in public**.
![get_token_2][GetToken2]

- query course id
- query assignment id
- get all students' unique id
- prepare your score file and modify the scripts

[GetToken0]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_token_0.png
[GetToken1]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_token_1.png
[GetToken2]: https://github.gatech.edu/khsu38/canvas_submission_api/blob/master/figs/get_token_2.png
