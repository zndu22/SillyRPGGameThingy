import pygame
import pygame_gui

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600
window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define screen layouts
VIEWPORT_RECT = pygame.Rect(0, 0, 750, 600)
SIDEBAR_RECT = pygame.Rect(750, 0, 250, 600)

ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# --- 1. MAIN SIDEBAR CONTAINER ---
sidebar_panel = pygame_gui.elements.UIPanel(
    relative_rect=SIDEBAR_RECT,
    starting_height=1,
    manager=ui_manager
)

# --- 2. DEFINE THE MENU CONTAINERS (PANELS) ---
# We make sub-panels inside the sidebar. They share the exact same space.
# We turn off "visible" by default for panels that shouldn't show at startup.

menu_rect = pygame.Rect((10, 10), (230, 480)) # Shared dimensions for menus

# A. Inventory Panel (Visible at start)
inv_panel = pygame_gui.elements.UIPanel(relative_rect=menu_rect, manager=ui_manager, container=sidebar_panel)
pygame_gui.elements.UILabel(pygame.Rect((10, 10), (210, 30)), "--- INVENTORY ---", ui_manager, inv_panel)
# Add inventory grid button slots here later

# B. Skills Panel
skills_panel = pygame_gui.elements.UIPanel(relative_rect=menu_rect, manager=ui_manager, container=sidebar_panel, visible=0)
pygame_gui.elements.UILabel(pygame.Rect((10, 10), (210, 30)), "--- SKILLS ---", ui_manager, skills_panel)
pygame_gui.elements.UILabel(pygame.Rect((10, 50), (210, 30)), "Attack: 99 / 99", ui_manager, skills_panel)

# C. Stats Panel
stats_panel = pygame_gui.elements.UIPanel(relative_rect=menu_rect, manager=ui_manager, container=sidebar_panel, visible=0)
pygame_gui.elements.UILabel(pygame.Rect((10, 10), (210, 30)), "--- STATS ---", ui_manager, stats_panel)

# D. Debug Panel
debug_panel = pygame_gui.elements.UIPanel(relative_rect=menu_rect, manager=ui_manager, container=sidebar_panel, visible=0)
pygame_gui.elements.UILabel(pygame.Rect((10, 10), (210, 30)), "--- DEBUG INFO ---", ui_manager, debug_panel)

# E. Settings Panel
settings_panel = pygame_gui.elements.UIPanel(relative_rect=menu_rect, manager=ui_manager, container=sidebar_panel, visible=0)
pygame_gui.elements.UILabel(pygame.Rect((10, 10), (210, 30)), "--- SETTINGS ---", ui_manager, settings_panel)


# --- 3. THE NAVIGATION BUTTONS ---
# Placed at the bottom of the sidebar panel (Y: 500)
btn_w, btn_h = 44, 40  # Small square-ish layout icons

btn_inv  = pygame_gui.elements.UIButton(pygame.Rect((10, 500),  (btn_w, btn_h)), "INV",  ui_manager, sidebar_panel)
btn_skl  = pygame_gui.elements.UIButton(pygame.Rect((54, 500),  (btn_w, btn_h)), "SKL",  ui_manager, sidebar_panel)
btn_stat = pygame_gui.elements.UIButton(pygame.Rect((98, 500),  (btn_w, btn_h)), "STA",  ui_manager, sidebar_panel)
btn_dbg  = pygame_gui.elements.UIButton(pygame.Rect((142, 500), (btn_w, btn_h)), "DBG",  ui_manager, sidebar_panel)
btn_set  = pygame_gui.elements.UIButton(pygame.Rect((186, 500), (btn_w, btn_h)), "SET",  ui_manager, sidebar_panel)


# --- 4. TABS MANAGER UTILITY ---
# Mapping buttons directly to their corresponding sub-panels
menu_tabs = {
    btn_inv: inv_panel,
    btn_skl: skills_panel,
    btn_stat: stats_panel,
    btn_dbg: debug_panel,
    btn_set: settings_panel
}

def switch_to_menu(active_button):
    """Hides all menus and makes only the selected one visible."""
    for button, panel in menu_tabs.items():
        if button == active_button:
            panel.show() # Make visible
        else:
            panel.hide() # Make invisible

# Main Game Loop
clock = pygame.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        ui_consumed = ui_manager.process_events(event)

        # Catch UI interactions
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            # Check if clicked button is one of our nav tabs
            if event.ui_element in menu_tabs:
                switch_to_menu(event.ui_element)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if ui_consumed:
                # The click hit a UI panel, button, or menu item
                print("UI Maintained: Processing inventory or store interaction.")
                continue

            # Check if the click happened inside the playable viewport boundaries
            if VIEWPORT_RECT.collidepoint(event.pos):
                # Translate screen coordinates into game grid coordinates
                grid_x = event.pos[0] // 32
                grid_y = event.pos[1] // 32
                print(f"Game Maintained: Player clicked grid tile ({grid_x}, {grid_y})")


    ui_manager.update(time_delta)

    window_surface.fill((30, 30, 30))
    pygame.draw.rect(window_surface, (50, 100, 50), VIEWPORT_RECT) # Game Viewport
    ui_manager.draw_ui(window_surface)

    pygame.display.update()

pygame.quit()
