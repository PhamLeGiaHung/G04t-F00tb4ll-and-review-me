from guizero import App, Text, Box
app = App(title = "Bảng danh sách học sinh", width =  480, height = 150, layout = "grid")
box_name = Box(app, grid = [0, 0, 6, 1], border = True)
text_name = Text(box_name, text = "                               Danh sách học sinh                                ", size = 14, color = "red")
for column in range(0, 6):
    for row in range(1, 5):
        box_content = Box(app, grid = [column, row], border = True, width = 80, height = 30)
        if row == 1:
            if column == 0:
                text_content = Text(box_content, text = "Tên")
            elif column == 1:
                text_content = Text(box_content, text = "Tuổi")
            elif column == 2:
                text_content = Text(box_content, text = "Trường")
            elif column == 3:
                text_content = Text(box_content, text = "Lớp")
            elif column == 4:
                text_content = Text(box_content, text = "Giới tính")
            elif column == 5:
                text_content = Text(box_content, text = "Sở thích")
        if row == 2:
            if column == 0:
                text_content = Text(box_content, text = "An")
            elif column == 1:
                text_content = Text(box_content, text = "12")
            elif column == 2:
                text_content = Text(box_content, text = "THCS C/Thắng")
            elif column == 3:
                text_content = Text(box_content, text = "7/2")
            elif column == 4:
                text_content = Text(box_content, text = "Nam")
            elif column == 5:
                text_content = Text(box_content, text = "Bóng đá")
        if row == 3:
            if column == 0:
                text_content = Text(box_content, text = "Bình")
            elif column == 1:
                text_content = Text(box_content, text = "12")
            elif column == 2:
                text_content = Text(box_content, text = "THCS C/Thắng")
            elif column == 3:
                text_content = Text(box_content, text = "7/5")
            elif column == 4:
                text_content = Text(box_content, text = "Nam")
            elif column == 5:
                text_content = Text(box_content, text = "Đọc sách")
        if row == 4:
            if column == 0:
                text_content = Text(box_content, text = "Khang")
            elif column == 1:
                text_content = Text(box_content, text = "12")
            elif column == 2:
                text_content = Text(box_content, text = "THCS C/Thắng")
            elif column == 3:
                text_content = Text(box_content, text = "7/3")
            elif column == 4:
                text_content = Text(box_content, text = "Nam")
            elif column == 5:
                text_content = Text(box_content, text = "Cờ Vua")

app.display()