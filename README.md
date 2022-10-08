# Possible MD -> HTML Conversions


## Using "Glow" + "aha"
Glow will convert MD to very pretty terminal output. Aha will take that and turn it into an ungodly inefficient HTML file (uses span for each color, can't blame it tho cuase the input is like that)
`script -q filename.txt glow README.md`
`cat filename.txt | aha --black > filename.html`

## Github action MD to HTML add style block that looks like Glow?
