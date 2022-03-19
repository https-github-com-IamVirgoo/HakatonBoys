<section class="hero">
    <container>
        <h1 class="container-heading">How it works?</h1>
        <p class="container-description">Программа представляет собой веб приложение, основной<br>скрипт которого написан на Python. Скрипт работает по<br>следующему принципу: Загружается база данных, скрипт<br>получает значения из базы и обрабатывает их согласно<br>написанной математической модели</p>
        <a href="/service#link" class="btn">Попробовать</a>
    </container>
</section>

<section id="link">
    <div class="container">
        <h2>Enter the link</h2>
        <p>Description that swe need to wait</p>
        <div class="btn--wrap">
            <input type="input" id="" placeholder="https://www.google.ru/sheets">
            <button type="submit">Подтвердить</button>
        </div>
    </div>
</section>

<section class="choose" id="choose">
    <div class="container">
        <h2>Choose the name of product</h2>
        <p>Description that swe need to wait</p>
        <div class="btn--wrap">
            <select type="input" id="">
                <option value="">first</option>
                <option value="">second</option>
                <option value="">third</option>
                <option value="">fourth</option>
                <option value="">fiveth</option>
                <option value="">sixth</option>
                <option value="">seventh</option>
            </select>
            <button type="submit">Подтвердить</button>
        </div>
    </div>
</section>

<section class="result" id="result">
    <div class="container">
        <h2>Result</h2>
        <div class="result-desc">
            <div class="res-left">
                <p class="description-left">В первое полугодие, на<br>основе загруженной базы<br>данных, выбранный вами<br>товар будет стоить [price]</p>
                <div class="icons">
                    <img src="./static/src/svg/dollar.svg" alt="">
                    <img src="./static/src/svg/ruble.svg" alt="">
                    <img src="./static/src/svg/euro.svg" alt="">
                </div>
            </div>
            <div class="res-center">
                <p class="description-center">Во втором полугодии, на<br>основе загруженной базы<br>данных, выбранный вами<br>товар будет стоить [price]</p>
                <div class="icons">
                    <img src="./static/src/svg/dollar.svg" alt="">
                    <img src="./static/src/svg/ruble.svg" alt="">
                    <img src="./static/src/svg/euro.svg" alt="">
                </div>
            </div>
            <div class="res-right">
                <p class="description-right">В ближайший год, на<br>основе загруженной базы<br>данных, выбранный вами<br>товар будет стоить [price]</p>
                <div class="icons">
                    <img src="./static/src/svg/dollar.svg" alt="">
                    <img src="./static/src/svg/ruble.svg" alt="">
                    <img src="./static/src/svg/euro.svg" alt="">
                </div>
            </div>
        </div>
    </div>
</section>
<script>
    let prices = fetch('hhtps://dolar-api.heroku.com/api/v1/testify')
</script>