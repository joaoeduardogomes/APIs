let playlists = [
    {
        id: 1,
        name: "Rock",
        tags: ["rock", "classic", "pop"],
        songs: [
            {
                id: 1,
                title: "Wonderwall",
                artist: "Oasis",
                year: 1995,
                album: "What's the Story (Morning Glory?)"
            },
            {
                id: 2,
                title: "Misery Business",
                artist: "Paramore",
                year: 2007,
                album: "Riot!"
            }
        ]
    }
];

let songsList = [
    {
        "id": 1,
        "title": "Wonderwall",
        "artist": "Oasis",
        "year": 1995,
        "album": "What's the Story (Morning Glory?)"
    },
    {
        "id": 2,
        "title": "Misery Business",
        "artist": "Paramore",
        "year": 2007,
        "album": "Riot!"
    },
    {
        "id": 3,
        "title": "Californication",
        "artist": "Red Hot Chili Peppers",
        "year": 1999,
        "album": "Californication"
    },
    {
        "id": 4,
        "title": "Thunderstruck",
        "artist": "AC/DC",
        "year": 1990,
        "album": "The Razor's Edge"
    },
    {
        "id": 5,
        "title": "Helena",
        "artist": "My Chemical Romance",
        "year": 2004,
        "album": "Three Cheers for Sweet Revenge"
    },
    {
        "id": 6,
        "title": "There Is a Light That Never Goes Out",
        "artist": "The Smiths",
        "year": 1986,
        "album": "The Queen Is Dead"
    },
    {
        "id": 7,
        "title": "Smells Like Teen Spirit",
        "artist": "Nirvana",
        "year": 1991,
        "album": "Nevermind"
    },
    {
        "id": 8,
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "year": 1975,
        "album": "A Night at the Opera"
    },
    {
        "id": 9,
        "title": "Sweet Child o' Mine",
        "artist": "Guns N' Roses",
        "year": 1987,
        "album": "Appetite for Destruction"
    },
    {
        "id": 10,
        "title": "Hotel California",
        "artist": "Eagles",
        "year": 1976,
        "album": "Hotel California"
    },
    {
        "id": 11,
        "title": "Stairway to Heaven",
        "artist": "Led Zeppelin",
        "year": 1971,
        "album": "Led Zeppelin IV"
    },
    {
        "id": 12,
        "title": "Billie Jean",
        "artist": "Michael Jackson",
        "year": 1982,
        "album": "Thriller"
    },
    {
        "id": 13,
        "title": "Creep",
        "artist": "Radiohead",
        "year": 1993,
        "album": "Pablo Honey"
    },
    {
        "id": 14,
        "title": "Losing My Religion",
        "artist": "R.E.M.",
        "year": 1991,
        "album": "Out of Time"
    },
    {
        "id": 15,
        "title": "I Wanna Dance with Somebody (Who Loves Me)",
        "artist": "Whitney Houston",
        "year": 1987,
        "album": "Whitney"
    }
];

function generateRandomID() {
    return Math.floor(Math.random() * 999999)
}

function findPlaylistById(id) {
    return playlists.find(pl => pl.id === +id)
}

module.exports = {
    getAllPlaylists: () => {
        return playlists;
    },

    getPlaylistById: (id) => {
        return findPlaylistById(id);
    },

    addNewPlaylist: (name, tags, songs) => {
        const newPlaylist = {
            id: generateRandomID(),
            name: name,
            tags: tags,
            songs: songs ?? []
        }

        playlists.push(newPlaylist);
        return newPlaylist;
    },

    updatePlaylistName: (id, name) => {
        const playlist = findPlaylistById(id);

        if (!playlist) return null;

        playlist.name = name;
        return playlist;
    },

    addTagToPlaylist: (id, tag) => {
        const playlist = findPlaylistById(id);

        if (!playlist) return null;

        if (playlist.tags.includes(tag)) return "Tag already exists";

        playlist.tags.push(tag);
        return playlist;
    },

    removeTagFromPlaylist: (id, tag) => {
        const playlist = findPlaylistById(id);

        if (!playlist) return null;

        if (!playlist.tags.includes(tag)) return "Tag not found";

        // removemos com 'filter' porque é uma string:
        playlist.tags = playlist.tags.filter(t => t !== tag);
        return playlist;
    },

    deletePlaylist: (id) => {
        const playlist = findPlaylistById(id);

        if (!playlist) return null;

        playlists = playlists.filter(p => p.id !== +id);
        return playlist;
    },

    addSongToPlaylist: (playlistId, songId) => {
        const playlist = findPlaylistById(playlistId);

        if (!playlist) return "Playlist not found";

        // usamos o 'find' porque esta função é mais simples:
        const song = songsList.find(song => song.id === +songId);

        if (!song) return "Song not found. Try to create it first.";

        if (playlist.songs.includes(song)) return "Song already exists";

        playlist.songs.push(song);
        return playlist;
    },

    removeSongFromPlaylist: (playlistId, songId) => {
        const playlist = findPlaylistById(playlistId);

        if (!playlist) return "Playlist not found";

        // Usamos o 'findIndex' porque esta função exige outro tratamento:
        const songIndex = playlist.songs.findIndex(song => song.id === +songId);

        if (songIndex === -1) return "Song not found";

        // Removemos com 'splice' porque é um objeto
        playlist.songs.splice(songIndex, 1);

        return playlist;
    },

    getAllSongs: () => {
        return songsList;
    },

    createNewSong: (title, artist, year, album) => {
        const newSong = {
            id: generateRandomID(),
            title: title,
            artist: artist,
            year: year,
            album: album
        }

        songsList.push(newSong);
        return newSong;
    },

    
};