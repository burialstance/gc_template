from litestar import Controller, get, Request, Response, status_codes, MediaType


class IndexPageController(Controller):
    path = '/'
    include_in_schema = False

    @get()
    async def index_page(self) -> Response:
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title></title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                text-align: center;
                padding: 50px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                color: #333;
            }
            .spinner {
                border: 4px solid rgba(0, 0, 0, 0.1);
                border-left-color: #333;
                border-radius: 50%;
                width: 40px;
                height: 40px;
                animation: spin 1s linear infinite;
                margin: 20px auto;
            }
            @keyframes spin {
                to {
                    transform: rotate(360deg);
                }
            }
            #quote {
                margin-top: 20px;
                font-style: italic;
                color: #555;
                max-width: 600px;
                padding: 0 20px;
            }
            .image-container {
                margin-top: 30px;
            }
            .image-container img {
                width: 512px;
                height: 512px;
                object-fit: cover;
                border-radius: 8px;
                # box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            
        </style>

        <body>
            <div class="image-container">
                <img src="https://www.pngplay.com/wp-content/uploads/9/Jason-Statham-PNG-Free-File-Download-1.png" alt="Пример изображения">
            </div>
            
            <p id="quote">счас ченить придумаю ...</p>

            <script>
                const stathamPhrases = [
                    'Слышал, что скупой платит дважды, теперь хочу работать у скупого.',
                    'Хмели сумели — и ты сможешь.',
                    'Шаг влево, шаг вправо — два шага.',
                    'Завтра рано вставать, встану послезавтра.',
                    'Однажды городской тип купил поселок. Теперь это поселок городского типа.',
                    'Если тебе где-то не рады в рваных носках, то и в целых туда идти не стоит.',
                    'Запомни: всего одна ошибка — и ты ошибся.',
                    'Делай, как надо. Как не надо, не делай.',
                    'Бабки не главное. Главное — их пенсия.',
                    'Человек меняется по двум причинам: или по первой, или по второй.',
                    'Не бойся, когда ты один. Бойся, когда тебя два.',
                    'Ехал на «девятке» и перевернулся — поехал дальше на «шестерке».',
                ];

                const quoteElement = document.getElementById('quote');

                function updateQuote() {
                    const randomIndex = Math.floor(Math.random() * stathamPhrases.length);
                    quoteElement.textContent = stathamPhrases[randomIndex];
                }

                setInterval(updateQuote, 5000);
                updateQuote();
            </script>
        </body>

        </html>
        """
        return Response(
            content=html_content,
            status_code=status_codes.HTTP_200_OK,
            media_type=MediaType.HTML
        )
