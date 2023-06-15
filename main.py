from flet import *

def main(page:Page):
    page.window_width=400
    page.padding = 0
    page.spacing = 0
    listtext = Column()


    # ADD LOOP TEXT
    for x in range(0,40):
        listtext.controls.append(
            Text(f"{x} data ",size=25)
            )

    def youfunctionscroll(e:OnScrollEvent):
        print(e)
        # NOW IF YOU SCROLL DOWN AFTER VALUE 60 
        # this text hai flet will change to youtube
        # and change size Container
        # now get name
        getname = page.controls[0].content.controls[0].controls[0].value
        # get scfoll value
        scroll_position = e.pixels
        target_opacity = 200

        if scroll_position > 60:
            # YOU EFFECT HERE
            target_opacity += 100
            page.controls[0].content.controls[0].controls[0].value = "Youtube"
            # AND CHANGE COLOR
            page.controls[0].content.controls[0].controls[0].color = "black"
            # AND CHANGE SIZE height
            page.controls[0].height -=10

            # AND CHANGE COLOR OPACITY CONTAINER
            # IF YOU SCROLL DOWN THIS COLOR WILL WEIGHT
            page.controls[0].bgcolor = f"red{target_opacity}"

            # AND IF YOU SCROLL AND GET HEIGHT < 50
            # THEN FIXED SIZE HEIGHT
            if page.controls[0].height < 50:
                page.controls[0].height = 50
                # AND CHANGE TEXT COLOR TO WHITE
                page.controls[0].content.controls[0].controls[0].color = "white"

        # NOW IF YOU SCROLL UP AGAIN THEN BACK TO START
        else:
            target_opacity -=100
            page.controls[0].content.controls[0].controls[0].color ="black"
            page.controls[0].content.controls[0].controls[0].value ="Hai Flet"
            # AND CHANGE COLOR TO BACK AGAIN
            page.controls[0].bgcolor= f"red{target_opacity}"
            page.controls[0].height = 80
        page.update()






    page.add(
        # NOW ADD APPBAR
        Container(
            margin=0,
            height=100,
            padding=10,
            # ADD SHADOW TO Container
            shadow = BoxShadow(
                spread_radius=1,
                blur_radius=15
                ),
            # ADD ANIMATION IF THIS Container
            # CHANGE SIZE 
            animate=animation.Animation(300,"easeIn"),
            bgcolor="red100",
            content=Column([
                Row([
                    Text("Hai Flet",size=30,
                    weight="bold",color="black"
                        )
                    ],alignment="center")
                ])
            ),

        Column([
            listtext
            ],
            # AND NOW ACTIVATE SCROLL IN COLUMN
            # AND SHOW VALUE OF YOU SCROLL
            scroll="always",
            on_scroll=youfunctionscroll,
            width=page.window_width,
            height=page.window_height

            )
        )
flet.app(target=main)
