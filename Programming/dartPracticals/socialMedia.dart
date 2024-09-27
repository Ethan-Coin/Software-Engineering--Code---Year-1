class Post {
  String content;
  String author;
  String date;

  Post(this.content, this.author, this.date);
}

class SocialMediaFeed {
  List<Post> posts = [];
  List<Post> liked = [];

  void add(Post post) {
    posts.add(post);
  }

  void remove(Post post) => posts.remove(post);

  void like(Post post) => liked.add(post);

  String toString() {
    String string = 'Feed:\n';
    for (Post post in posts) {}
  }
}
