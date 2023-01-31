<template>
    <nav class="navbar navbar-expand-lg navbar-dark" style="background: repeating-linear-gradient(45deg, #0e1122, #0e1122 10px, #20264c 10px, #20264c 20px);">
        <div class="container">
            <router-link class="nav-link " to="/" style="color: azure;"> Training Notes</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/dashboard"> Доска событий </router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link "  href="/calender"> Календарь </a>
                    </li>
                    <li class="nav-item" >
                        <div class="collapse navbar-collapse" id="navbarNavDarkDropdown" >
                            <ul class="navbar-nav" >
                                <li class="nav-item dropdown" >
                                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    События
                                </a>
                                <ul class="dropdown-menu" style="background: repeating-linear-gradient(45deg, #0e1122, #0e1122 10px, #20264c 10px, #20264c 20px);">
                                    <li class="dropdown-item"><router-link class="nav-link "  to="/article-form"> Все </router-link></li>
                                    <li class="dropdown-item"><router-link class="nav-link "  to="/article-form"> Текущие </router-link></li>
                                    <li class="dropdown-item"><router-link class="nav-link "  to="/article-form"> Предстоящие </router-link></li>
                                    <li class="dropdown-item"><router-link class="nav-link "  to="/article-form"> Завершенные </router-link></li>
                                </ul>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/article-form"> Статистика </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/article-form"> Программы </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/article-form"> Упражнения </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/article-form"> Измерения </router-link>
                    </li>
                    <li class="nav-item">
                            <a class="nav-link " href="/admin/login"> Admin panel </a>    
                        

                    </li >
                    <li class="nav-item">
                        <div class="collapse navbar-collapse" id="navbarNavDarkDropdown">
                            <ul class="navbar-nav">
                                <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    request.user
                                </a>
                                <ul class="dropdown-menu" style="background: repeating-linear-gradient(45deg, #0e1122, #0e1122 10px, #20264c 10px, #20264c 20px);">
                                    <li class="dropdown-item"><router-link class="nav-link "  to="/article-form"> Настройки пользователя </router-link></li>
                                    <li class="dropdown-item"><router-link class="nav-link "  to="/article-form"> Профиль </router-link></li>
                                    <li class="dropdown-item"><a class="nav-link "  href="/accounts/signout"> Выйти </a></li>
                                </ul>
                                </li>
                            </ul>
                        </div>
                    </li >
                </ul>
            </div>
            
        </div>
        
    </nav>

</template>
<script>

export default{
    name:'header-nav'
}
</script>