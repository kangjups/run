using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneController : MonoBehaviour
{
    public void Replay()
    {
        GameManager.gameStarted = false;
        SceneManager.LoadScene("PlayScene");
    }

    public void Home()
    {
        GameManager.gameStarted = false;
        SceneManager.LoadScene("Home");
    }

    public void Exit()
    {
#if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
#else
        Application.Quit();
#endif
    }
}