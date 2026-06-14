function toggleTheme() {

    document.documentElement.classList.toggle(
        "dark-mode"
    );

    if (
        document.documentElement.classList.contains(
            "dark-mode"
        )
    ) {

        localStorage.setItem(
            "theme",
            "dark"
        );

    } else {

        localStorage.setItem(
            "theme",
            "light"
        );
    }
}