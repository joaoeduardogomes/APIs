const playlistModel = require("../models/playlistModel");

module.exports = {
    //* GET /playlists
    index: (req, res) => {
        const playlists = playlistModel.getAllPlaylists();

        res.status(200).json(playlists);
    },

    //* GET /playlists/:playlistId
        // tem que parrar "playlistId" direitinho nos parâmetros, pois é como estána rota.
        // um erro que ocorreu foi passar apenas "id"
    showPlaylist: (req, res) => {
        const { playlistId } = req.params;
        
        const playlist = playlistModel.getPlaylistById(playlistId);
    
        if (!playlist) {
            return res.status(404).json({ message: "Playlist not found" });
        }
    
        res.status(200).json(playlist);
    },

    //* POST /playlists
    savePlaylist: (req, res) => {
        const {name, tags, songs} = req.body;

        if (typeof name !== "string") 
            return res.status(400).json({message: "Name must be a string"});
        if (Array.isArray(tags) === false)
            return res.status(400).json({message: "Tags must be an array"});
        if (songs && (Array.isArray(songs) === false))
            return res.status(400).json({message: "Songs must be an array"});

        const newPlaylist = playlistModel.addNewPlaylist(name, tags, songs);
        res.status(201).json(newPlaylist);
    },

    //* PATCH name /playlists/update-name/:playlistId
    updatePlaylistName: (req, res) => {
        const {playlistId} = req.params;
        const {name} = req.body;

        if (!name) return res.status(400).json({message: "Name is required"});
        
        const playlist = playlistModel.updatePlaylistName(playlistId, name);

        if (!playlist)
            return res.status(404).json({message: "Playlist not found"});
        
        res.json(playlist);
    },

    //* PATCH add tag /playlists/tags/add/:playlistId
    addTagToPlaylist: (req, res) => {
        const {playlistId} = req.params;
        const {tag} = req.body;

        if (!tag) return res.status(400).json({message: "A tag is required"});
        if (typeof tag !== "string") return res.status(400).json({message: "The new tag must be a string"});

        const playlist = playlistModel.addTagToPlaylist(playlistId, tag);

        if (!playlist) 
            return res.status(404).json({message: "Playlist not found"});

        if (playlist === "Tag already exists")
            return res.status(400).json({message: "Tag already exists"});

        res.json(playlist);
    },

    //* PATCH remove tag /playlists/tags/remove/:playlistId
    removeTagFromPlaylist: (req, res) => {
        const {playlistId} = req.params;
        const {tag} = req.body;

        if (!tag) return res.status(400).json({message: "A tag is required"});
        if (typeof tag !== "string") return res.status(400).json({message: "The tag name must be a string"});

        const playlist = playlistModel.removeTagFromPlaylist(playlistId, tag);

        if (!playlist)
            return res.status(404).json({message: "Playlist not found"});

        if (playlist === "Tag not found")
            return res.status(400).json({message: "Tag not found"});

        res.json(playlist);
    },

    //* DELETE /playlists/:playlistId
    deletePlaylist: (req, res) => {
        const {playlistId} = req.params;

        const playlist = playlistModel.deletePlaylist(playlistId);

        if (!playlist) return res.status(404).json({message: "Playlist not found"});

        res.status(200).json(playlist);
    },

    //* POST song to playlist /playlists/:playlistId/songs/:songId
    addSongToPlaylist: (req, res) => {
        const {playlistId, songId} = req.params;

        const playlist = playlistModel.addSongToPlaylist(playlistId, songId);

        if (typeof playlist === "string")
            return res.status(400).json({message: playlist});
        
        res.status(200).json(playlist);
    },

    //* DELETE song from playlist /playlists/:playlistId/songs/:songId
    removeSongFromPlaylist: (req, res) => {
        const {playlistId, songId} = req.params;

        const playlist = playlistModel.removeSongFromPlaylist(playlistId, songId);

        if (typeof playlist === "string")
            return res.status(404).json({message: playlist});
        
        res.status(200).json(playlist);
    },

    //* GET all songs /songs
    showSongs: (req, res) => {
        const songs = playlistModel.getAllSongs();

        res.status(200).json(songs);
    },

    //* POST new song /songs
    saveSong: (req, res) => {
        const {title, artist, year, album} = req.body;

        const newSong = playlistModel.createNewSong(title, artist, year, album);

        res.status(201).json(newSong);
    },

};