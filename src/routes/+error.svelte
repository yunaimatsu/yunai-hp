<script>
    import { page } from '$app/stores';
    import '$lib/global.css';
</script>

<h1>{$page.status}: {$page.error ? $page.error.message : 'No message'}</h1>

<p>Go back to <a href="/">home</a></p>