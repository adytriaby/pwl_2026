<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\WelcomeController;
use App\Http\Controllers\PageController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\AboutController;
use App\Http\Controllers\ArticleController;

// Praktikum 1 - Basic Routing
Route::get('/hello', [WelcomeController::class, 'hello']);
Route::get('/world', function () {
    return 'World';
});

// Praktikum 1 - Tambahan route
Route::get('/praktikum-home', [PageController::class, 'index']);
Route::get('/praktikum-about', [PageController::class, 'about']);

// Praktikum 1 - Route Parameters
Route::get('/user/{name}', function ($name) {
    return 'Nama saya '.$name;
});

Route::get('/posts/{post}/comments/{comment}', function ($postId, $commentId) {
    return 'Pos ke-'.$postId.' Komentar ke-: '.$commentId;
});

Route::get('/articles/{id}', [PageController::class, 'articles']);

// Praktikum 1 - Optional Parameters
Route::get('/user-optional/{name?}', function ($name = 'John') {
    return 'Nama saya '.$name;
});

// Praktikum 2 - Controller
Route::get('/greeting', [WelcomeController::class, 'greeting']);

// Praktikum 2 - PageController
Route::get('/', [PageController::class, 'index']);
Route::get('/about', [PageController::class, 'about']);

// Praktikum 2 - Single Action Controller
Route::get('/single-home', HomeController::class);
Route::get('/single-about', AboutController::class);
Route::get('/single-articles/{id}', ArticleController::class);
