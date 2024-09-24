const express = require('express');
const playlistController = require('./controllers/playlistController');

const router = express.Router();

router.get("/playlists", playlistController.index);
router.get("/playlists/:playlistId", playlistController.showPlaylist);
router.get("/songs", playlistController.showSongs);

router.post("/playlists", playlistController.savePlaylist);
router.post("/playlists/:playlistId/songs/:songId", playlistController.addSongToPlaylist);
router.post("/songs", playlistController.saveSong);

router.patch("/playlists/update-name/:playlistId", playlistController.updatePlaylistName);
router.patch("/playlists/tags/add/:playlistId", playlistController.addTagToPlaylist);
router.patch("/playlists/tags/remove/:playlistId", playlistController.removeTagFromPlaylist);

router.delete("/playlists/:playlistId", playlistController.deletePlaylist);
router.delete("/playlists/:playlistId/songs/:songId", playlistController.removeSongFromPlaylist);


module.exports = router;