<script>

</script>
<div class="navbar">
    <p id="title">yunai</p>

    <nav class="nav-menu">
        <a href="/cs">Computer Science</a>
        <a href="/economics">Economcis</a>
        <a href="/linguistics">Linguistics</a>
        <a href="mailto:yunaimatsu@gmail.com">Email</a>
        <a href="https://github.com/yunaimatsu">GitHub</a>
        <a href="https://twitter.com/supegoroshiago">Twitter</a>
    </nav>
</div>

<slot />

<footer>
    <p style="font-family: 'Times New Roman', Times, serif;">yunai official</p>
    <a href="mailto:yunaimatsu@gmail.com">Email</a>
    
    <a href="https://github.com/yunaimatsu">GitHub</a>
    <a href="https://twitter.com/supegoroshiago">Twitter</a>
</footer>

<style>
    .navbar {
        background-color: #333;
        color: white;
        font-family: 'Roboto', serif;
        padding: 0.5em;
        text-align: center;
        margin: 0;
    }

    #title {
        font-size: 3em;
    }

    p {
        margin: 0;
    }

    footer {
        background-color: #EEEEEE;
        color: #303030;
        font-size: 1.5em;
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

    a {
        color: #0077cc;
        text-decoration: none;
    }

    a:hover {
        color: #005999;
    }

    .nav-menu {
        display: flex;
        gap: 1rem;
    }
</style>