## Solution
This Solution5.md4 video illustrates that the solution was comprised of simply adding the humao.rest-client entry to the extensions sections in the devcontainer.json file:

```json
	"extensions": [
		"ms-python.python",
		"ms-python.vscode-pylance",
		"humao.rest-client"
	],
```

## From the Field
When developing REST APIs, we take advantage of the rest-client and maintain a *.http file for manual testing.  This **does not** replace the requirements for automated unit, integration and acceptance testing.