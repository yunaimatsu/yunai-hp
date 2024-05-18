<script>
    let showMenu = false;

    function toggleMenu() {
    showMenu = !showMenu;
    }
</script>
<div class="navbar">
    <a id="title" href="/">yunai</a >

    <nav class="nav-menu">
        <a href="ability">Ability</a>
        <a href="about">About Me</a>
    </nav>
</div>
<button class="hamburger" on:click={toggleMenu}>
    <span>&#9776;</span>
</button>

<slot />

<footer>
    <p style="font-family: 'Times New Roman', Times, serif;" class="footer-title">yunai official</p>
    <a href="mailto:yunaimatsu@gmail.com">Email</a>
    <a href="https://github.com/yunaimatsu">GitHub</a>
    <a href="https://twitter.com/supegoroshiago">Twitter</a>
</footer>

<style>
    .navbar {
        background-color: #333;
        color: white;
        font-family: 'Roboto', serif;
        text-align: center;
    }

    #title {
        font-size: 3em;
        margin: 0.5em 1em;
        color: #CCC;
        text-decoration: none;
    }

    p {
        margin: 0;
    }

    footer {
        background-color: #CCC;
        color: #303030;
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
    }

    .nav-menu > a {
        color: #0077cc;
        text-decoration: none;
    }

    .nav-menu > a:hover {
        color: #005999;
    }

    .nav-menu {
        display: flex;
        gap: 1rem;
    }

    .footer-title {
        margin-left: 1em;
    }

    @media only screen and (width <= 600px) {
        .nav-menu {
            visibility: hidden;
        }
    }
    @media only screen and (300px <= width <= 600px) {
    }
</style>