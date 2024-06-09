<script>
    import '$lib/style/global.css';
</script>

<main>
    <div class="body">
        <div class="container">
            <p class="notion">Please visit my <a href="https://yunaimatsu.notion.site/Information-3334f559a4534428bd16afbc37f4af2d?pvs=4" class="notion-link">Notion</a></p>
            <div class="item" id="hardware">
                <h2>Hardware</h2>
            </div>
            <div class="item" id="software">
                <h2>Software</h2>
            </div>
        </div>
    </div>
</main>
<style>
    .body {
        font-family: 'Roboto', sans-serif;
        color: #444;
        background-color: #f5f5f5;
    }

    .notion {
        padding: 20px;
    }

    main {
        padding: 20px;
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .item {
        background-color: #fff;
        border-radius: 3px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
        margin: 20px;
        padding: 20px;
        width: 50%;
        flex-direction: column;
    }

    h2 {
        padding: 10px;
        font-family: 'Roboto', sans-serif;
        color: #333;
    }

    a {
        color: #0077cc;
        text-decoration: none;
    }

    a:hover {
        color: #005999;
    }
</style>