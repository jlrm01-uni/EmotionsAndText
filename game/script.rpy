
define e = Character("Eileen")

style dramatic_text is text:
    size 90

image big_text = ParameterizedText(style="dramatic_text")

image eileen smile = im.Scale("eileen smile.png", 800, 600)
image eileen shocked = im.Scale("eileen shocked.png", 800, 600)
image eileen poisoned = im.Scale("eileen poisoned.png", 800, 600)

label start:

    show eileen smile

    show big_text "This is very dramatic" at truecenter
    pause 2
    hide big_text

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    show eileen shocked

    e "Once you add a story, pictures, and music, you can release it to the world!"

    show eileen poisoned

    e "blah blah blah"

    # This ends the game.

    return
