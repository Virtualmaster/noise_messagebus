Rails.application.routes.draw do
  get 'noise_levels/run_script' => 'noise_levels#run_script'
  get 'noise_levels/listen_to' => "noise_levels#listen_to"
  resources :noise_levels

  root to: "noise_levels#index"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
