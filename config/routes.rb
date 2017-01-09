Rails.application.routes.draw do
  get 'noise_levels/run_script' => 'noise_levels#run_script'
  resources :noise_levels

  root to: "noise_levels#index"
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
