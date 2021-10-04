## Solution
This solution4.md4 video illustrates that the solution was comprised of adding 2 sections to the devcontainer.json file, the forwardPorts and portsAttributes sections:

```json
	"forwardPorts": [5000],

	"portsAttributes": {
		"5000": {
			"label": "MathAPI"
		}
	},
```