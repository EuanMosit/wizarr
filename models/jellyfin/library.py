# Generated by https://quicktype.io

from enum import Enum
from uuid import UUID
from datetime import datetime
from typing import List, Dict


class PuneHedgehog(Enum):
    STRING = "string"


class AlbumArtist:
    name: PuneHedgehog
    id: UUID

    def __init__(self, name: PuneHedgehog, id: UUID) -> None:
        self.name = name
        self.id = id


class Chapter:
    start_position_ticks: int
    name: PuneHedgehog
    image_path: PuneHedgehog
    image_date_modified: datetime
    image_tag: PuneHedgehog

    def __init__(self, start_position_ticks: int, name: PuneHedgehog, image_path: PuneHedgehog, image_date_modified: datetime, image_tag: PuneHedgehog) -> None:
        self.start_position_ticks = start_position_ticks
        self.name = name
        self.image_path = image_path
        self.image_date_modified = image_date_modified
        self.image_tag = image_tag


class ExternalURL:
    name: PuneHedgehog
    url: PuneHedgehog

    def __init__(self, name: PuneHedgehog, url: PuneHedgehog) -> None:
        self.name = name
        self.url = url


class ImageTags:
    additional_prop1: PuneHedgehog
    additional_prop2: PuneHedgehog
    additional_prop3: PuneHedgehog

    def __init__(self, additional_prop1: PuneHedgehog, additional_prop2: PuneHedgehog, additional_prop3: PuneHedgehog) -> None:
        self.additional_prop1 = additional_prop1
        self.additional_prop2 = additional_prop2
        self.additional_prop3 = additional_prop3


class MediaAttachment:
    codec: PuneHedgehog
    codec_tag: PuneHedgehog
    comment: PuneHedgehog
    index: int
    file_name: PuneHedgehog
    mime_type: PuneHedgehog
    delivery_url: PuneHedgehog

    def __init__(self, codec: PuneHedgehog, codec_tag: PuneHedgehog, comment: PuneHedgehog, index: int, file_name: PuneHedgehog, mime_type: PuneHedgehog, delivery_url: PuneHedgehog) -> None:
        self.codec = codec
        self.codec_tag = codec_tag
        self.comment = comment
        self.index = index
        self.file_name = file_name
        self.mime_type = mime_type
        self.delivery_url = delivery_url


class MediaStream:
    codec: PuneHedgehog
    codec_tag: PuneHedgehog
    language: PuneHedgehog
    color_range: PuneHedgehog
    color_space: PuneHedgehog
    color_transfer: PuneHedgehog
    color_primaries: PuneHedgehog
    dv_version_major: int
    dv_version_minor: int
    dv_profile: int
    dv_level: int
    rpu_present_flag: int
    el_present_flag: int
    bl_present_flag: int
    dv_bl_signal_compatibility_id: int
    comment: PuneHedgehog
    time_base: PuneHedgehog
    codec_time_base: PuneHedgehog
    title: PuneHedgehog
    video_range: PuneHedgehog
    video_range_type: PuneHedgehog
    video_do_vi_title: PuneHedgehog
    localized_undefined: PuneHedgehog
    localized_default: PuneHedgehog
    localized_forced: PuneHedgehog
    localized_external: PuneHedgehog
    display_title: PuneHedgehog
    nal_length_size: PuneHedgehog
    is_interlaced: bool
    is_avc: bool
    channel_layout: PuneHedgehog
    bit_rate: int
    bit_depth: int
    ref_frames: int
    packet_length: int
    channels: int
    sample_rate: int
    is_default: bool
    is_forced: bool
    height: int
    width: int
    average_frame_rate: int
    real_frame_rate: int
    profile: PuneHedgehog
    type: str
    aspect_ratio: PuneHedgehog
    index: int
    score: int
    is_external: bool
    delivery_method: str
    delivery_url: PuneHedgehog
    is_external_url: bool
    is_text_subtitle_stream: bool
    supports_external_stream: bool
    path: PuneHedgehog
    pixel_format: PuneHedgehog
    level: int
    is_anamorphic: bool

    def __init__(self, codec: PuneHedgehog, codec_tag: PuneHedgehog, language: PuneHedgehog, color_range: PuneHedgehog, color_space: PuneHedgehog, color_transfer: PuneHedgehog, color_primaries: PuneHedgehog, dv_version_major: int, dv_version_minor: int, dv_profile: int, dv_level: int, rpu_present_flag: int, el_present_flag: int, bl_present_flag: int, dv_bl_signal_compatibility_id: int, comment: PuneHedgehog, time_base: PuneHedgehog, codec_time_base: PuneHedgehog, title: PuneHedgehog, video_range: PuneHedgehog, video_range_type: PuneHedgehog, video_do_vi_title: PuneHedgehog, localized_undefined: PuneHedgehog, localized_default: PuneHedgehog, localized_forced: PuneHedgehog, localized_external: PuneHedgehog, display_title: PuneHedgehog, nal_length_size: PuneHedgehog, is_interlaced: bool, is_avc: bool, channel_layout: PuneHedgehog, bit_rate: int, bit_depth: int, ref_frames: int, packet_length: int, channels: int, sample_rate: int, is_default: bool, is_forced: bool, height: int, width: int, average_frame_rate: int, real_frame_rate: int, profile: PuneHedgehog, type: str, aspect_ratio: PuneHedgehog, index: int, score: int, is_external: bool, delivery_method: str, delivery_url: PuneHedgehog, is_external_url: bool, is_text_subtitle_stream: bool, supports_external_stream: bool, path: PuneHedgehog, pixel_format: PuneHedgehog, level: int, is_anamorphic: bool) -> None:
        self.codec = codec
        self.codec_tag = codec_tag
        self.language = language
        self.color_range = color_range
        self.color_space = color_space
        self.color_transfer = color_transfer
        self.color_primaries = color_primaries
        self.dv_version_major = dv_version_major
        self.dv_version_minor = dv_version_minor
        self.dv_profile = dv_profile
        self.dv_level = dv_level
        self.rpu_present_flag = rpu_present_flag
        self.el_present_flag = el_present_flag
        self.bl_present_flag = bl_present_flag
        self.dv_bl_signal_compatibility_id = dv_bl_signal_compatibility_id
        self.comment = comment
        self.time_base = time_base
        self.codec_time_base = codec_time_base
        self.title = title
        self.video_range = video_range
        self.video_range_type = video_range_type
        self.video_do_vi_title = video_do_vi_title
        self.localized_undefined = localized_undefined
        self.localized_default = localized_default
        self.localized_forced = localized_forced
        self.localized_external = localized_external
        self.display_title = display_title
        self.nal_length_size = nal_length_size
        self.is_interlaced = is_interlaced
        self.is_avc = is_avc
        self.channel_layout = channel_layout
        self.bit_rate = bit_rate
        self.bit_depth = bit_depth
        self.ref_frames = ref_frames
        self.packet_length = packet_length
        self.channels = channels
        self.sample_rate = sample_rate
        self.is_default = is_default
        self.is_forced = is_forced
        self.height = height
        self.width = width
        self.average_frame_rate = average_frame_rate
        self.real_frame_rate = real_frame_rate
        self.profile = profile
        self.type = type
        self.aspect_ratio = aspect_ratio
        self.index = index
        self.score = score
        self.is_external = is_external
        self.delivery_method = delivery_method
        self.delivery_url = delivery_url
        self.is_external_url = is_external_url
        self.is_text_subtitle_stream = is_text_subtitle_stream
        self.supports_external_stream = supports_external_stream
        self.path = path
        self.pixel_format = pixel_format
        self.level = level
        self.is_anamorphic = is_anamorphic


class MediaSource:
    protocol: str
    id: PuneHedgehog
    path: PuneHedgehog
    encoder_path: PuneHedgehog
    encoder_protocol: str
    type: str
    container: PuneHedgehog
    size: int
    name: PuneHedgehog
    is_remote: bool
    e_tag: PuneHedgehog
    run_time_ticks: int
    read_at_native_framerate: bool
    ignore_dts: bool
    ignore_index: bool
    gen_pts_input: bool
    supports_transcoding: bool
    supports_direct_stream: bool
    supports_direct_play: bool
    is_infinite_stream: bool
    requires_opening: bool
    open_token: PuneHedgehog
    requires_closing: bool
    live_stream_id: PuneHedgehog
    buffer_ms: int
    requires_looping: bool
    supports_probing: bool
    video_type: str
    iso_type: str
    video3_d_format: str
    media_streams: List[MediaStream]
    media_attachments: List[MediaAttachment]
    formats: List[PuneHedgehog]
    bitrate: int
    timestamp: str
    required_http_headers: ImageTags
    transcoding_url: PuneHedgehog
    transcoding_sub_protocol: PuneHedgehog
    transcoding_container: PuneHedgehog
    analyze_duration_ms: int
    default_audio_stream_index: int
    default_subtitle_stream_index: int

    def __init__(self, protocol: str, id: PuneHedgehog, path: PuneHedgehog, encoder_path: PuneHedgehog, encoder_protocol: str, type: str, container: PuneHedgehog, size: int, name: PuneHedgehog, is_remote: bool, e_tag: PuneHedgehog, run_time_ticks: int, read_at_native_framerate: bool, ignore_dts: bool, ignore_index: bool, gen_pts_input: bool, supports_transcoding: bool, supports_direct_stream: bool, supports_direct_play: bool, is_infinite_stream: bool, requires_opening: bool, open_token: PuneHedgehog, requires_closing: bool, live_stream_id: PuneHedgehog, buffer_ms: int, requires_looping: bool, supports_probing: bool, video_type: str, iso_type: str, video3_d_format: str, media_streams: List[MediaStream], media_attachments: List[MediaAttachment], formats: List[PuneHedgehog], bitrate: int, timestamp: str, required_http_headers: ImageTags, transcoding_url: PuneHedgehog, transcoding_sub_protocol: PuneHedgehog, transcoding_container: PuneHedgehog, analyze_duration_ms: int, default_audio_stream_index: int, default_subtitle_stream_index: int) -> None:
        self.protocol = protocol
        self.id = id
        self.path = path
        self.encoder_path = encoder_path
        self.encoder_protocol = encoder_protocol
        self.type = type
        self.container = container
        self.size = size
        self.name = name
        self.is_remote = is_remote
        self.e_tag = e_tag
        self.run_time_ticks = run_time_ticks
        self.read_at_native_framerate = read_at_native_framerate
        self.ignore_dts = ignore_dts
        self.ignore_index = ignore_index
        self.gen_pts_input = gen_pts_input
        self.supports_transcoding = supports_transcoding
        self.supports_direct_stream = supports_direct_stream
        self.supports_direct_play = supports_direct_play
        self.is_infinite_stream = is_infinite_stream
        self.requires_opening = requires_opening
        self.open_token = open_token
        self.requires_closing = requires_closing
        self.live_stream_id = live_stream_id
        self.buffer_ms = buffer_ms
        self.requires_looping = requires_looping
        self.supports_probing = supports_probing
        self.video_type = video_type
        self.iso_type = iso_type
        self.video3_d_format = video3_d_format
        self.media_streams = media_streams
        self.media_attachments = media_attachments
        self.formats = formats
        self.bitrate = bitrate
        self.timestamp = timestamp
        self.required_http_headers = required_http_headers
        self.transcoding_url = transcoding_url
        self.transcoding_sub_protocol = transcoding_sub_protocol
        self.transcoding_container = transcoding_container
        self.analyze_duration_ms = analyze_duration_ms
        self.default_audio_stream_index = default_audio_stream_index
        self.default_subtitle_stream_index = default_subtitle_stream_index


class Person:
    name: PuneHedgehog
    id: UUID
    role: PuneHedgehog
    type: PuneHedgehog
    primary_image_tag: PuneHedgehog
    image_blur_hashes: Dict[str, ImageTags]

    def __init__(self, name: PuneHedgehog, id: UUID, role: PuneHedgehog, type: PuneHedgehog, primary_image_tag: PuneHedgehog, image_blur_hashes: Dict[str, ImageTags]) -> None:
        self.name = name
        self.id = id
        self.role = role
        self.type = type
        self.primary_image_tag = primary_image_tag
        self.image_blur_hashes = image_blur_hashes


class UserData:
    rating: int
    played_percentage: int
    unplayed_item_count: int
    playback_position_ticks: int
    play_count: int
    is_favorite: bool
    likes: bool
    last_played_date: datetime
    played: bool
    key: PuneHedgehog
    item_id: PuneHedgehog

    def __init__(self, rating: int, played_percentage: int, unplayed_item_count: int, playback_position_ticks: int, play_count: int, is_favorite: bool, likes: bool, last_played_date: datetime, played: bool, key: PuneHedgehog, item_id: PuneHedgehog) -> None:
        self.rating = rating
        self.played_percentage = played_percentage
        self.unplayed_item_count = unplayed_item_count
        self.playback_position_ticks = playback_position_ticks
        self.play_count = play_count
        self.is_favorite = is_favorite
        self.likes = likes
        self.last_played_date = last_played_date
        self.played = played
        self.key = key
        self.item_id = item_id


class JellyfinLibraryItem:
    name: PuneHedgehog
    original_title: PuneHedgehog
    server_id: PuneHedgehog
    id: UUID
    etag: PuneHedgehog
    source_type: PuneHedgehog
    playlist_item_id: PuneHedgehog
    date_created: datetime
    date_last_media_added: datetime
    extra_type: PuneHedgehog
    airs_before_season_number: int
    airs_after_season_number: int
    airs_before_episode_number: int
    can_delete: bool
    can_download: bool
    has_subtitles: bool
    preferred_metadata_language: PuneHedgehog
    preferred_metadata_country_code: PuneHedgehog
    supports_sync: bool
    container: PuneHedgehog
    sort_name: PuneHedgehog
    forced_sort_name: PuneHedgehog
    video3_d_format: str
    premiere_date: datetime
    external_urls: List[ExternalURL]
    media_sources: List[MediaSource]
    critic_rating: int
    production_locations: List[PuneHedgehog]
    path: PuneHedgehog
    enable_media_source_display: bool
    official_rating: PuneHedgehog
    custom_rating: PuneHedgehog
    channel_id: UUID
    channel_name: PuneHedgehog
    overview: PuneHedgehog
    taglines: List[PuneHedgehog]
    genres: List[PuneHedgehog]
    community_rating: int
    cumulative_run_time_ticks: int
    run_time_ticks: int
    play_access: str
    aspect_ratio: PuneHedgehog
    production_year: int
    is_place_holder: bool
    number: PuneHedgehog
    channel_number: PuneHedgehog
    index_number: int
    index_number_end: int
    parent_index_number: int
    remote_trailers: List[ExternalURL]
    provider_ids: ImageTags
    is_hd: bool
    is_folder: bool
    parent_id: UUID
    type: str
    people: List[Person]
    studios: List[AlbumArtist]
    genre_items: List[AlbumArtist]
    parent_logo_item_id: UUID
    parent_backdrop_item_id: UUID
    parent_backdrop_image_tags: List[PuneHedgehog]
    local_trailer_count: int
    user_data: UserData
    recursive_item_count: int
    child_count: int
    series_name: PuneHedgehog
    series_id: UUID
    season_id: UUID
    special_feature_count: int
    display_preferences_id: PuneHedgehog
    status: PuneHedgehog
    air_time: PuneHedgehog
    air_days: List[str]
    tags: List[PuneHedgehog]
    primary_image_aspect_ratio: int
    artists: List[PuneHedgehog]
    artist_items: List[AlbumArtist]
    album: PuneHedgehog
    collection_type: PuneHedgehog
    display_order: PuneHedgehog
    album_id: UUID
    album_primary_image_tag: PuneHedgehog
    series_primary_image_tag: PuneHedgehog
    album_artist: PuneHedgehog
    album_artists: List[AlbumArtist]
    season_name: PuneHedgehog
    media_streams: List[MediaStream]
    video_type: str
    part_count: int
    media_source_count: int
    image_tags: ImageTags
    backdrop_image_tags: List[PuneHedgehog]
    screenshot_image_tags: List[PuneHedgehog]
    parent_logo_image_tag: PuneHedgehog
    parent_art_item_id: UUID
    parent_art_image_tag: PuneHedgehog
    series_thumb_image_tag: PuneHedgehog
    image_blur_hashes: Dict[str, ImageTags]
    series_studio: PuneHedgehog
    parent_thumb_item_id: UUID
    parent_thumb_image_tag: PuneHedgehog
    parent_primary_image_item_id: PuneHedgehog
    parent_primary_image_tag: PuneHedgehog
    chapters: List[Chapter]
    location_type: str
    iso_type: str
    media_type: PuneHedgehog
    end_date: datetime
    locked_fields: List[str]
    trailer_count: int
    movie_count: int
    series_count: int
    program_count: int
    episode_count: int
    song_count: int
    album_count: int
    artist_count: int
    music_video_count: int
    lock_data: bool
    width: int
    height: int
    camera_make: PuneHedgehog
    camera_model: PuneHedgehog
    software: PuneHedgehog
    exposure_time: int
    focal_length: int
    image_orientation: str
    aperture: int
    shutter_speed: int
    latitude: int
    longitude: int
    altitude: int
    iso_speed_rating: int
    series_timer_id: PuneHedgehog
    program_id: PuneHedgehog
    channel_primary_image_tag: PuneHedgehog
    start_date: datetime
    completion_percentage: int
    is_repeat: bool
    episode_title: PuneHedgehog
    channel_type: str
    audio: str
    is_movie: bool
    is_sports: bool
    is_series: bool
    is_live: bool
    is_news: bool
    is_kids: bool
    is_premiere: bool
    timer_id: PuneHedgehog
    current_program: PuneHedgehog

    def __init__(self, name: PuneHedgehog, original_title: PuneHedgehog, server_id: PuneHedgehog, id: UUID, etag: PuneHedgehog, source_type: PuneHedgehog, playlist_item_id: PuneHedgehog, date_created: datetime, date_last_media_added: datetime, extra_type: PuneHedgehog, airs_before_season_number: int, airs_after_season_number: int, airs_before_episode_number: int, can_delete: bool, can_download: bool, has_subtitles: bool, preferred_metadata_language: PuneHedgehog, preferred_metadata_country_code: PuneHedgehog, supports_sync: bool, container: PuneHedgehog, sort_name: PuneHedgehog, forced_sort_name: PuneHedgehog, video3_d_format: str, premiere_date: datetime, external_urls: List[ExternalURL], media_sources: List[MediaSource], critic_rating: int, production_locations: List[PuneHedgehog], path: PuneHedgehog, enable_media_source_display: bool, official_rating: PuneHedgehog, custom_rating: PuneHedgehog, channel_id: UUID, channel_name: PuneHedgehog, overview: PuneHedgehog, taglines: List[PuneHedgehog], genres: List[PuneHedgehog], community_rating: int, cumulative_run_time_ticks: int, run_time_ticks: int, play_access: str, aspect_ratio: PuneHedgehog, production_year: int, is_place_holder: bool, number: PuneHedgehog, channel_number: PuneHedgehog, index_number: int, index_number_end: int, parent_index_number: int, remote_trailers: List[ExternalURL], provider_ids: ImageTags, is_hd: bool, is_folder: bool, parent_id: UUID, type: str, people: List[Person], studios: List[AlbumArtist], genre_items: List[AlbumArtist], parent_logo_item_id: UUID, parent_backdrop_item_id: UUID, parent_backdrop_image_tags: List[PuneHedgehog], local_trailer_count: int, user_data: UserData, recursive_item_count: int, child_count: int, series_name: PuneHedgehog, series_id: UUID, season_id: UUID, special_feature_count: int, display_preferences_id: PuneHedgehog, status: PuneHedgehog, air_time: PuneHedgehog, air_days: List[str], tags: List[PuneHedgehog], primary_image_aspect_ratio: int, artists: List[PuneHedgehog], artist_items: List[AlbumArtist], album: PuneHedgehog, collection_type: PuneHedgehog, display_order: PuneHedgehog, album_id: UUID, album_primary_image_tag: PuneHedgehog, series_primary_image_tag: PuneHedgehog, album_artist: PuneHedgehog, album_artists: List[AlbumArtist], season_name: PuneHedgehog, media_streams: List[MediaStream], video_type: str, part_count: int, media_source_count: int, image_tags: ImageTags, backdrop_image_tags: List[PuneHedgehog], screenshot_image_tags: List[PuneHedgehog], parent_logo_image_tag: PuneHedgehog, parent_art_item_id: UUID, parent_art_image_tag: PuneHedgehog, series_thumb_image_tag: PuneHedgehog, image_blur_hashes: Dict[str, ImageTags], series_studio: PuneHedgehog, parent_thumb_item_id: UUID, parent_thumb_image_tag: PuneHedgehog, parent_primary_image_item_id: PuneHedgehog, parent_primary_image_tag: PuneHedgehog, chapters: List[Chapter], location_type: str, iso_type: str, media_type: PuneHedgehog, end_date: datetime, locked_fields: List[str], trailer_count: int, movie_count: int, series_count: int, program_count: int, episode_count: int, song_count: int, album_count: int, artist_count: int, music_video_count: int, lock_data: bool, width: int, height: int, camera_make: PuneHedgehog, camera_model: PuneHedgehog, software: PuneHedgehog, exposure_time: int, focal_length: int, image_orientation: str, aperture: int, shutter_speed: int, latitude: int, longitude: int, altitude: int, iso_speed_rating: int, series_timer_id: PuneHedgehog, program_id: PuneHedgehog, channel_primary_image_tag: PuneHedgehog, start_date: datetime, completion_percentage: int, is_repeat: bool, episode_title: PuneHedgehog, channel_type: str, audio: str, is_movie: bool, is_sports: bool, is_series: bool, is_live: bool, is_news: bool, is_kids: bool, is_premiere: bool, timer_id: PuneHedgehog, current_program: PuneHedgehog) -> None:
        self.name = name
        self.original_title = original_title
        self.server_id = server_id
        self.id = id
        self.etag = etag
        self.source_type = source_type
        self.playlist_item_id = playlist_item_id
        self.date_created = date_created
        self.date_last_media_added = date_last_media_added
        self.extra_type = extra_type
        self.airs_before_season_number = airs_before_season_number
        self.airs_after_season_number = airs_after_season_number
        self.airs_before_episode_number = airs_before_episode_number
        self.can_delete = can_delete
        self.can_download = can_download
        self.has_subtitles = has_subtitles
        self.preferred_metadata_language = preferred_metadata_language
        self.preferred_metadata_country_code = preferred_metadata_country_code
        self.supports_sync = supports_sync
        self.container = container
        self.sort_name = sort_name
        self.forced_sort_name = forced_sort_name
        self.video3_d_format = video3_d_format
        self.premiere_date = premiere_date
        self.external_urls = external_urls
        self.media_sources = media_sources
        self.critic_rating = critic_rating
        self.production_locations = production_locations
        self.path = path
        self.enable_media_source_display = enable_media_source_display
        self.official_rating = official_rating
        self.custom_rating = custom_rating
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.overview = overview
        self.taglines = taglines
        self.genres = genres
        self.community_rating = community_rating
        self.cumulative_run_time_ticks = cumulative_run_time_ticks
        self.run_time_ticks = run_time_ticks
        self.play_access = play_access
        self.aspect_ratio = aspect_ratio
        self.production_year = production_year
        self.is_place_holder = is_place_holder
        self.number = number
        self.channel_number = channel_number
        self.index_number = index_number
        self.index_number_end = index_number_end
        self.parent_index_number = parent_index_number
        self.remote_trailers = remote_trailers
        self.provider_ids = provider_ids
        self.is_hd = is_hd
        self.is_folder = is_folder
        self.parent_id = parent_id
        self.type = type
        self.people = people
        self.studios = studios
        self.genre_items = genre_items
        self.parent_logo_item_id = parent_logo_item_id
        self.parent_backdrop_item_id = parent_backdrop_item_id
        self.parent_backdrop_image_tags = parent_backdrop_image_tags
        self.local_trailer_count = local_trailer_count
        self.user_data = user_data
        self.recursive_item_count = recursive_item_count
        self.child_count = child_count
        self.series_name = series_name
        self.series_id = series_id
        self.season_id = season_id
        self.special_feature_count = special_feature_count
        self.display_preferences_id = display_preferences_id
        self.status = status
        self.air_time = air_time
        self.air_days = air_days
        self.tags = tags
        self.primary_image_aspect_ratio = primary_image_aspect_ratio
        self.artists = artists
        self.artist_items = artist_items
        self.album = album
        self.collection_type = collection_type
        self.display_order = display_order
        self.album_id = album_id
        self.album_primary_image_tag = album_primary_image_tag
        self.series_primary_image_tag = series_primary_image_tag
        self.album_artist = album_artist
        self.album_artists = album_artists
        self.season_name = season_name
        self.media_streams = media_streams
        self.video_type = video_type
        self.part_count = part_count
        self.media_source_count = media_source_count
        self.image_tags = image_tags
        self.backdrop_image_tags = backdrop_image_tags
        self.screenshot_image_tags = screenshot_image_tags
        self.parent_logo_image_tag = parent_logo_image_tag
        self.parent_art_item_id = parent_art_item_id
        self.parent_art_image_tag = parent_art_image_tag
        self.series_thumb_image_tag = series_thumb_image_tag
        self.image_blur_hashes = image_blur_hashes
        self.series_studio = series_studio
        self.parent_thumb_item_id = parent_thumb_item_id
        self.parent_thumb_image_tag = parent_thumb_image_tag
        self.parent_primary_image_item_id = parent_primary_image_item_id
        self.parent_primary_image_tag = parent_primary_image_tag
        self.chapters = chapters
        self.location_type = location_type
        self.iso_type = iso_type
        self.media_type = media_type
        self.end_date = end_date
        self.locked_fields = locked_fields
        self.trailer_count = trailer_count
        self.movie_count = movie_count
        self.series_count = series_count
        self.program_count = program_count
        self.episode_count = episode_count
        self.song_count = song_count
        self.album_count = album_count
        self.artist_count = artist_count
        self.music_video_count = music_video_count
        self.lock_data = lock_data
        self.width = width
        self.height = height
        self.camera_make = camera_make
        self.camera_model = camera_model
        self.software = software
        self.exposure_time = exposure_time
        self.focal_length = focal_length
        self.image_orientation = image_orientation
        self.aperture = aperture
        self.shutter_speed = shutter_speed
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.iso_speed_rating = iso_speed_rating
        self.series_timer_id = series_timer_id
        self.program_id = program_id
        self.channel_primary_image_tag = channel_primary_image_tag
        self.start_date = start_date
        self.completion_percentage = completion_percentage
        self.is_repeat = is_repeat
        self.episode_title = episode_title
        self.channel_type = channel_type
        self.audio = audio
        self.is_movie = is_movie
        self.is_sports = is_sports
        self.is_series = is_series
        self.is_live = is_live
        self.is_news = is_news
        self.is_kids = is_kids
        self.is_premiere = is_premiere
        self.timer_id = timer_id
        self.current_program = current_program


class JellyfinLibrary:
    items: List[JellyfinLibraryItem]
    total_record_count: int
    start_index: int

    def __init__(self, items: List[JellyfinLibraryItem], total_record_count: int, start_index: int) -> None:
        self.items = items
        self.total_record_count = total_record_count
        self.start_index = start_index