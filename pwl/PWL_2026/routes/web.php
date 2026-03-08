<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;
use App\Http\Controllers\PageController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\AboutController;
use App\Http\Controllers\ArticleController;

Route::get('/hello', [WelcomeController::class, 'hello']);
Route::get('/world', function () {
    return 'World';
});

Route::get('/', [PageController::class, 'index']);
Route::get('/about', [PageController::class, 'about']);

Route::get('/user/{name}', function ($name) {
    return 'Nama saya '.$name;
});

Route::get('/posts/{post}/comments/{comment}', function ($postId, $commentId) {
    return 'Pos ke-'.$postId.' Komentar ke-: '.$commentId;
});

Route::get('/articles/{id}', [PageController::class, 'articles']);

Route::get('/user-optional/{name?}', function ($name = 'John') {
    return 'Nama saya '.$name;
});

Route::get('/greeting', [WelcomeController::class, 'greeting']);

Route::get('/single-home', HomeController::class);
Route::get('/single-about', AboutController::class);
Route::get('/single-articles/{id}', ArticleController::class);
