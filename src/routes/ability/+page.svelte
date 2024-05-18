<script>
    let showMenu = false;

    function toggleMenu() {
    showMenu = !showMenu;
}
</script>
<div class="container">
    <a class="item" href="ability/language">言語</a>
    <a class="item" href="ability/dx">Notion</a>
    <a class="item" href="ability/cs">情報工学</a>
    <a class="item" href="ability/humainities">人文学</a>
    <a class="item" href="ability/economics">経済学</a>
</div>

<style>
    * {
        font-family: 'Roboto', sans-serif;
    }
    .container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        padding: 1rem;
    }

    .item {
        font-size: 2em;
        color: #666;
        text-align: center;
        justify-content: center;
        padding: 3rem;
        border-style: solid;
        border-width: 1px;
        border-color: #BBB;
        font-weight: bold;
    }

    /* For tablets: */
    @media only screen and (width <= 600px) {
        .container {
            grid-template-columns: 1fr; /* two columns for tablets */
            padding: 1em;
        }
    }
    @media only screen and (600px <= width <= 900px) {
        .container {
            grid-template-columns: repeat(2, 1fr); /* two columns for tablets */
            padding: 1.5em;
        }
    }

    /* For desktop: */
    @media only screen and (900px <= width) {
        .container {
            grid-template-columns: repeat(3, 1fr); /* three columns for desktop */
            padding: 2em;
        }
    }
</style>