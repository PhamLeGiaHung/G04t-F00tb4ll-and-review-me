from guizero import App, Text, Box, Picture

app = App(title="Album cầu thủ bóng đá nổi tiếng", width=800, height=700, layout="grid", bg="lightblue")

title = Text(app, text="⚽ Album cầu thủ bóng đá nổi tiếng ⚽", size=16, color="red", grid=[0,0,4,1])

players = [
    ("goatronaldo.png", "Ronaldo", "Bồ Đào Nha", "Tiền đạo"),
    ("goatmessi.png", "Messi", "Argentina", "Tiền đạo"),
    ("goatyamal.png", "Yamal", "Tây Ban Nha", "Tiền đạo")
]

Text(Box(app, grid=[0,1], width=180, height=50, border=True), text="Hình ảnh", color="blue", size=12)

for i, (img, name, nation, pos) in enumerate(players, start=1):
    Text(Box(app, grid=[i,1], width=200, height=50, border=True), text=name, color="blue", size=12)

    Picture(Box(app, grid=[i,2], width=200, height=200, border=True), image=img, width=180, height=180)

    info = Box(app, grid=[i,3], width=200, height=100)
    Text(info, text=f"Quốc gia: {nation}", size=11)
    Text(info, text=f"Vị trí: {pos}", size=11)

app.display()
