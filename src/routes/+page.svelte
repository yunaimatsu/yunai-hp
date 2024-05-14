<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<div class="navbar">
    <a href="/cs">Computer Science</a>
    <a href="/economics">Economcis</a>
    <a href="/linguistics">Linguistics</a>
</div>

<style>
    .navbar {
        display: grid;
        gap: 1rem;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: 1fr;
    }
    h1 {
        color: #333;
    }
    p {
        color: #666;
    }
    a {
        color: #0070f3;
    }
</style>