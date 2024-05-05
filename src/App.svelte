<script>
	export let name;
</script>
<main>
	<h1 class="title">Hello {name}!</h1>
	<p class="description">Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
	<a href="/economics">Click here</a>
	<p class="class1">Allow me to introduce myself. My name is [Your Name] and I am a software developer with expertise in [Your Expertise]. I am passionate about creating high-quality software solutions and constantly expanding my knowledge in the field. Feel free to explore my projects and get in touch with me if you have any questions or collaboration opportunities.</p>
</main>
<style>
	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
		padding: 2em;
		background-color: #f2f2f2;
	}

	.title {
		color: #00004b;
		font-size: 3em;
		font-weight: bold;
		margin-bottom: 1em;
	}

	.description {
		font-size: 1.2em;
		text-align: center;
	}	

	a {
		color: #00004b;
		text-decoration: none;
	}

	.introduction {
		font-size: 2.0em;
		text-align: center;
		margin-top: 2em;
		padding: 1em;
		border-radius: 8px;
		background-color: #f9f9f9;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
	}

	.class1 {
		column-count: 2;
		text-align: center;
		column-fill: auto;
	}
	@media (min-width: 640px) {
		main {
			margin: 0 auto;
		}
	}
</style>