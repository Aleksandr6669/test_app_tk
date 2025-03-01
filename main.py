import flet as ft

def main(page: ft.Page):
    canvas_html = """
    <html>
    <body>
    <canvas id="myCanvas" width="200" height="200"></canvas>
    <script>
        var c = document.getElementById("myCanvas");
        var ctx = c.getContext("2d");

        // Тело кота
        ctx.fillStyle = "gray";
        ctx.beginPath();
        ctx.arc(100, 150, 50, 0, 2 * Math.PI);
        ctx.fill();

        // Голова кота
        ctx.beginPath();
        ctx.arc(100, 80, 40, 0, 2 * Math.PI);
        ctx.fill();

        // Глаза
        ctx.fillStyle = "white";
        ctx.beginPath();
        ctx.arc(85, 70, 10, 0, 2 * Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(115, 70, 10, 0, 2 * Math.PI);
        ctx.fill();

        ctx.fillStyle = "black";
        ctx.beginPath();
        ctx.arc(85, 70, 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(115, 70, 5, 0, 2 * Math.PI);
        ctx.fill();
    </script>
    </body>
    </html>
    """

    webview = ft.WebView(content=canvas_html, width=200, height=200)

    page.add(webview)

ft.app(target=main)