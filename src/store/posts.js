import { writable } from 'svelte/store';
import db from '../db';

interface Post {
  slug: string;
  title: string;
  date: string;
  content: string;
}

const posts = writable<Post[]>([]);

export async function fetchPosts(): Promise<void> {
  const { rows } = await db.query<Post>('SELECT * FROM posts');
  posts.set(rows);
}

export default posts;
