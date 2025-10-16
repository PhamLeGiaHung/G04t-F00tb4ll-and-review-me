from guizero import App, Text, Box, Picture
app = App(title = "Album cầu thủ bóng đá nổi tiếng", width = 800, height = 630, layout = "grid")
box_name = Box(app, grid = [0, 0, 4, 1], border = True)
text_name = Text(box_name, text = "                                                    Album cầu thủ bóng đá nổi tiếng                                                     ", size = 14, color = "red")
for column in range(0, 4):
    for row in range(1, 5):
        box_content = Box(app, grid = [column, row], border = True, width = 200, height = 150)
        if column == 0:
            if row == 1:
                text_content = Text(box_content, text = "Hình ảnh")
            elif row == 2:
                text_content = Text(box_content, text = "Tên")
            elif row == 3:
                text_content = Text(box_content, text = "Quốc gia") 
            elif row == 4:
                text_content = Text(box_content, text = "Vị trí trong đội bóng")
        elif column == 1:
            if row == 1:
                text_content = Picture(box_content, image = "goatronaldo.png", width = 200, height = 200)
            elif row == 2:
                text_content = Text(box_content, text = "Ronaldo")
            elif row == 3:
                text_content = Text(box_content, text = "Bồ Đào Nha") 
            elif row == 4:
                text_content = Text(box_content, text = "Tiền đạo")
        elif column == 2:
            if row == 1:
                text_content = Picture(box_content, image = "goatmessi.png", width = 200, height = 200)
            elif row == 2:
                text_content = Text(box_content, text = "Messi")
            elif row == 3:
                text_content = Text(box_content, text = "Argentina") 
            elif row == 4:
                text_content = Text(box_content, text = "Tiền đạo")
        elif column == 3:
            if row == 1:
                text_content = Picture(box_content, image = "goatyamal.png", width = 200, height = 200)
            elif row == 2:
                text_content = Text(box_content, text = "Yamal")
            elif row == 3:
                text_content = Text(box_content, text = "Tây Ban Nha") 
            elif row == 4:
                text_content = Text(box_content, text = "Tiền đạo")

app.display()