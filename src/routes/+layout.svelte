<script>
</script>
<div class="navbar">
    <a id="title" href="/">YuNai</a >
</div>
<slot />

<footer>
    <p style="font-family: 'Times New Roman', Times, serif;" class="footer-title">yunai official</p>
    <p class="lgroup">Contact</p>
    <div class="f-container">
        <a href="mailto:yunaimatsu@gmail.com" class="f-item">Email</a>
        <a href="https://github.com/yunaimatsu" class="f-item">GitHub</a>
        <a href="https://twitter.com/supegoroshiago" class="f-item">Twitter</a>
        <a href="https://www.linkedin.com/in/yoshihiro-matsuura-22179a302/" class="f-item">LinkedIn</a>
    </div>
    <p class="lgroup">Language</p>
    <div class="f-container">
        <a href="ability/language/typology" class="f-item">Language List</a>
        <a href="ability/language/linguistics" class="f-item">Linguistics</a>
        <a href="ability/cs" class="f-item">情報工学</a> 
        <a href="ability/humainities" class="f-item">人文学</a>
        <a href="ability/economics" class="f-item">経済学</a>
    <p>© 2024 yunai</p>
</footer>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100..900;1,100..900&display=swap');

    * {
        color: #FFF;
        text-shadow: 0 0 5px gray, 0 0 10px gray, 0 0 15px gray, 0 0 20px gray, 0 0 30px gray, 0 0 40px gray;

    }
    .navbar {
        height: 2em;
        background-color: #333;
        color: white;
        font-family: 'Roboto', serif;
        text-align: center;
        top: 0;
        left: 0;
        width: 100%;    
    }

    #title {
    font-family: "Exo 2", sans-serif;
    font-size: 1.5em;
    font-weight: 900;
    margin: 0.5em 1em;
    color: #FFF;
    text-decoration: none;
}

#title:hover {
    color: orange;
    text-shadow: 0 0 5px white, 0 0 10px white, 0 0 15px white, 0 0 20px white, 0 0 30px white, 0 0 40px white;
}

    p {
        margin: 0;
    }

    footer {
        font-size: 1em;
        font-family: 'Roboto', serif;
        padding: 0.5em;
        margin: 0;
    }

    .navbar {
        display: flex;
        gap: 1rem;
        justify-content: center;
        align-items: center;
        padding: 1rem;
        background: black;
        color: white;
    }

    .lgroup {
        font-weight: bold;
    }

    .footer-title {
        margin-left: 1em;
    }

    .f-container {
        padding: 1em;
        margin: 1em 3em 1em 3em;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
    }

    .f-item {
        text-align: center;
        justify-content: center;
        padding: 1rem;
        font-weight: bold;
        text-decoration: none;
    }

    @media only screen and (width <= 600px) {
        .f-container {
            grid-template-columns: 1fr;
            padding: 1em;
        }
    }
    @media only screen and (300px <= width <= 600px) {
    }
</style>