<script>
  // import '$lib/styles/global.css';
  import Loader from '$lib/Loader.svelte';
  import { onMount } from 'svelte';
  let isLoading = true;

  // Function to simulate loading data
  function loadData() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 3000); // Simulate loading data for 3 seconds
    });
  }

  // Set a minimum display time for the loader
  const minimumDisplayTime = 2000; // Minimum display time in milliseconds

  // Function to wait for both data load and minimum display time
  async function handleLoading() {
    const loadDataPromise = loadData();
    const minimumDisplayTimePromise = new Promise((resolve) => setTimeout(resolve, minimumDisplayTime));

    // Wait for both promises to resolve
    await Promise.all([loadDataPromise, minimumDisplayTimePromise]);
    isLoading = false;
  }

  // Call handleLoading on component mount
  onMount(() => {
    handleLoading();
  });
</script>

{#if isLoading}
  <Loader {isLoading} />
{:else}
  <div class="navbar">
    <div class="navbar__title">
      <a href="/">Yoshi</a>
    </div>
    <div class="navbar__github">
      <a href="https://github.com/yunaimatsu">
        <div>
          <svg width="3em" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8C0 11.54 2.29 14.53 5.47 15.59C5.87 15.66 6.02 15.42 6.02 15.21C6.02 15.02 6.01 14.39 6.01 13.72C4 14.09 3.48 13.23 3.32 12.78C3.23 12.55 2.84 11.84 2.5 11.65C2.22 11.5 1.82 11.13 2.49 11.12C3.12 11.11 3.57 11.7 3.72 11.94C4.44 13.15 5.59 12.81 6.05 12.6C6.12 12.08 6.33 11.73 6.56 11.53C4.78 11.33 2.92 10.64 2.92 7.58C2.92 6.71 3.23 5.99 3.74 5.43C3.66 5.23 3.38 4.41 3.82 3.31C3.82 3.31 4.49 3.1 6.02 4.13C6.66 3.95 7.34 3.86 8.02 3.86C8.7 3.86 9.38 3.95 10.02 4.13C11.55 3.09 12.22 3.31 12.22 3.31C12.66 4.41 12.38 5.23 12.3 5.43C12.81 5.99 13.12 6.7 13.12 7.58C13.12 10.65 11.25 11.33 9.47 11.53C9.76 11.78 10.01 12.26 10.01 13.01C10.01 14.08 10 14.94 10 15.21C10 15.42 10.15 15.67 10.55 15.59C13.71 14.53 16 11.53 16 8C16 3.58 12.42 0 8 0Z" fill="#FFFFFF"/>
          </svg>
        </div>
      </a>
    </div>
  </div>
  <slot />

  <footer>
    <p>© 2024 Yoshi</p>
  </footer>
{/if}

<!-- <style>
  .navbar {
    position: fixed;
    height: var(--navbar-height);
    width: 100%;
    background: linear-gradient(135deg, #006d77, #83c5be);
    opacity: 90%;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 1em;
    box-sizing: border-box;
    z-index: 1000;
  }
  
  .navbar__title {
    text-align: center;
  }

  .navbar__title a {
    font-family: "Exo 2", sans-serif;
    font-size: 1.5em;
    font-weight: 900;
    text-decoration: none;
    color: #FFFFFF;
  }

  .navbar__github {
    display: flex;
    align-items: center;
  }

  .navbar__github svg {
    fill: #FFFFFF;
  }

  footer {
    padding: 2em;
    background-color: #006d77;
    color: #FFFFFF;
    text-align: center;
    font-family: 'Roboto', serif;
    font-size: 0.9em;
  }
</style> -->
