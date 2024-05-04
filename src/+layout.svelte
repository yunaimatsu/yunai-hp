<script>
    /** @type {import('./$types').LayoutData} */
    let layoutData;
</script>

<style>
    /* Add your styles here */
</style>

<h1>Settings</h1>

<div class="submenu">
	{#each data.sections as section}
		<a href="/settings/{section.slug}">{section.title}</a>
	{/each}
</div>

<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/settings">Settings</a>
</nav>

<slot />